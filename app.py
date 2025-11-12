import gradio as gr
import os
from voices import VOICE_CONFIG
from text_processor import extract_text_pdf, extract_text_epub, clean_text, split_text_into_chunks
from audio_processor import convert_chunks_to_audio, concatenate_audio, save_audio

def get_file_type(filename):
    if filename.lower().endswith('.pdf'):
        return 'PDF'
    elif filename.lower().endswith('.epub'):
        return 'EPUB'
    return None

def extract_text(file_path, file_type):
    if file_type == 'PDF':
        return extract_text_pdf(file_path)
    elif file_type == 'EPUB':
        return extract_text_epub(file_path)
    return None

def generate_output_filename(input_filename, language, narrator):
    base_name = os.path.splitext(os.path.basename(input_filename))[0]
    lang_short = language.split()[0]
    narrator_short = narrator.split()[0].lower()
    return f"{base_name}_audiobook_{lang_short}_{narrator_short}.wav"

def convert_to_audiobook(file_upload, language, narrator, progress=gr.Progress()):
    if file_upload is None:
        return None, "Please select a file."
    
    if language not in VOICE_CONFIG:
        return None, "Unsupported language selected."
    
    lang_code = VOICE_CONFIG[language]["lang_code"]
    voice_code = VOICE_CONFIG[language]["voices"].get(narrator)
    
    if not voice_code:
        return None, "Invalid narrator selected."
    
    try:
        file_type = get_file_type(file_upload.name)
        if not file_type:
            return None, "Unsupported format. Use PDF or EPUB only."
        
        progress(0.1, desc="Extracting text...")
        raw_text = extract_text(file_upload.name, file_type)
        
        if not raw_text:
            return None, f"Could not extract text from {file_type}."
        
        progress(0.2, desc="Cleaning text...")
        clean_text_content = clean_text(raw_text)
        
        if len(clean_text_content) < 10:
            return None, "Extracted text too short."
        
        chunks = split_text_into_chunks(clean_text_content, chunk_size=200)
        
        progress(0.3, desc=f"Processing {len(chunks)} audio chunks...")
        
        def update_progress(completed, total):
            progress(0.3 + (completed / total) * 0.6, 
                   desc=f"Processed {completed}/{total} chunks")
        
        audio_results = convert_chunks_to_audio(
            chunks, voice_code, lang_code, 
            progress_callback=update_progress, 
            max_workers=4
        )
        
        if not audio_results:
            return None, "No audio was generated."
        
        progress(0.9, desc="Concatenating final audio...")
        complete_audio = concatenate_audio(audio_results)
        
        if complete_audio is None:
            return None, "No valid audio chunks."
        
        output_file = generate_output_filename(file_upload.name, language, narrator)
        duration = save_audio(complete_audio, output_file)
        
        progress(1.0, desc="Completed!")
        
        status_message = (
            f"✅ Audiobook created successfully!\n"
            f"📖 File: {file_type}\n"
            f"🌍 Language: {language}\n"
            f"🎭 Narrator: {narrator}\n"
            f"⏱️ Duration: {duration:.2f} seconds\n"
            f"📁 Text size: {len(clean_text_content)} characters"
        )
        
        return output_file, status_message
        
    except Exception as e:
        return None, f"❌ Error during conversion: {str(e)}"

def update_narrator_choices(language):
    if language in VOICE_CONFIG:
        choices = list(VOICE_CONFIG[language]["voices"].keys())
        return gr.Dropdown(
            choices=choices,
            value=choices[0] if choices else None,
            label="🎭 Select Narrator",
            info=f"Choose the voice for {language}"
        )
    return gr.Dropdown(choices=[])

def create_interface():
    with gr.Blocks(title="Audiobook Converter") as app:
        gr.HTML("""
        <div style="text-align: center; padding: 20px;">
            <h1>📚 Audiobook Converter</h1>
            <p>Convert your PDF or EPUB books into audiobooks with multilingual AI voices!</p>
            <p><strong>Supports 9 languages and 40+ voices powered by Kokoro TTS</strong></p>
            <p><em>⚠️ Note: Processing may take several minutes depending on book length</em></p>
        </div>
        """)
        
        with gr.Row():
            with gr.Column(scale=1):
                file_input = gr.File(
                    label="📁 Select your book",
                    file_types=[".pdf", ".epub"],
                    type="filepath"
                )
                
                language_input = gr.Dropdown(
                    choices=list(VOICE_CONFIG.keys()),
                    value="🇧🇷 Brazilian Portuguese (Default)",
                    label="🌍 Select Language",
                    info="Choose the language for narration"
                )
                
                narrator_input = gr.Dropdown(
                    choices=list(VOICE_CONFIG["🇧🇷 Brazilian Portuguese (Default)"]["voices"].keys()),
                    value="Dora (Female)",
                    label="🎭 Select Narrator",
                    info="Choose the voice that will narrate your audiobook"
                )
                
                convert_btn = gr.Button(
                    "🎵 Convert to Audiobook", 
                    variant="primary",
                    size="lg"
                )
            
            with gr.Column(scale=1):
                status_output = gr.Textbox(
                    label="📋 Conversion Status",
                    lines=8,
                    interactive=False
                )
                
                download_output = gr.File(
                    label="📥 Download Audiobook",
                    visible=True
                )
        
        # Examples section
        gr.HTML("""
        <div style="margin-top: 20px; padding: 15px; background-color: #f8f9fa; border-radius: 10px;">
            <h3 style="margin-top: 0;">💡 Tips for best results:</h3>
            <ul style="margin-bottom: 0;">
                <li>📄 <strong>PDF files:</strong> Works best with text-based PDFs (not scanned images)</li>
                <li>📚 <strong>EPUB files:</strong> Full support for all EPUB formats</li>
                <li>🎭 <strong>Voice selection:</strong> Try different voices to find your preferred style</li>
                <li>⏰ <strong>Processing time:</strong> Small books ~2-5 min, larger books ~10-20 min</li>
                <li>🎵 <strong>Output:</strong> High-quality 24kHz WAV files ready for any audio player</li>
            </ul>
        </div>
        """)
        
        language_input.change(
            fn=update_narrator_choices,
            inputs=[language_input],
            outputs=[narrator_input]
        )
        
        convert_btn.click(
            fn=convert_to_audiobook,
            inputs=[file_input, language_input, narrator_input],
            outputs=[download_output, status_output],
            show_progress="full"
        )    
    return app

if __name__ == "__main__":
    app = create_interface()
    app.launch(
        share=True,
        show_error=True,
        show_api=False
    )