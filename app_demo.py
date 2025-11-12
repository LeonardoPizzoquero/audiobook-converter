import gradio as gr
import os
import re
import PyPDF2
import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup

# Simplified voice config for demo
VOICE_CONFIG = {
    "🇧🇷 Brazilian Portuguese": {
        "lang_code": "p",
        "voices": {"Dora (Female)": "pf_dora", "Alex (Male)": "pm_alex", "Santa (Male)": "pm_santa"}
    },
    "🇺🇸 American English": {
        "lang_code": "a", 
        "voices": {"Bella (Female)": "af_bella", "Michael (Male)": "am_michael"}
    }
}

def extract_text_pdf(pdf_path):
    full_text = ""
    try:
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            for page in pdf_reader.pages:
                page_text = page.extract_text()
                if page_text:
                    full_text += page_text + "\n"
    except Exception as e:
        return f"Error reading PDF: {e}"
    return full_text

def extract_text_epub(epub_path):
    full_text = ""
    try:
        book = epub.read_epub(epub_path)
        items = list(book.get_items_of_type(ebooklib.ITEM_DOCUMENT))
        for item in items:
            content = item.get_content()
            soup = BeautifulSoup(content, 'html.parser')
            for script in soup(["script", "style"]):
                script.decompose()
            text = soup.get_text()
            if text:
                full_text += text + "\n"
    except Exception as e:
        return f"Error reading EPUB: {e}"
    return full_text

def clean_text(text):
    if not text:
        return ""
    text = re.sub(r'\n+', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^\w\s\.\,\!\?\;\:\-\(\)\"\']+', ' ', text)
    return text.strip()

def process_book(file_upload, language, narrator, progress=gr.Progress()):
    try:
        if file_upload is None:
            return None, "Please select a file."
        
        # Determine file type
        filename = file_upload.name.lower()
        progress(0.1, desc="Extracting text...")
        
        if filename.endswith('.pdf'):
            raw_text = extract_text_pdf(file_upload.name)
            file_type = "PDF"
        elif filename.endswith('.epub'):
            raw_text = extract_text_epub(file_upload.name)
            file_type = "EPUB"
        else:
            return None, "Unsupported format. Use PDF or EPUB only."
        
        if "Error" in str(raw_text):
            return None, raw_text
        
        progress(0.5, desc="Cleaning text...")
        clean_text_content = clean_text(raw_text)
        
        if len(clean_text_content) < 10:
            return None, "Extracted text too short."
        
        # Limit for demo
        if len(clean_text_content) > 2000:
            clean_text_content = clean_text_content[:2000] + "..."
        
        progress(0.8, desc="Preparing output...")
        
        # Create text file output (since we can't do TTS without Kokoro)
        output_filename = f"extracted_text_{file_type.lower()}.txt"
        with open(output_filename, 'w', encoding='utf-8') as f:
            f.write(clean_text_content)
        
        progress(1.0, desc="Completed!")
        
        status_message = (
            f"✅ Text extracted successfully!\n"
            f"📖 File: {file_type}\n"
            f"🌍 Language: {language}\n"
            f"🎭 Selected Narrator: {narrator}\n"
            f"📁 Text size: {len(clean_text_content)} characters\n\n"
            f"⚠️ Note: This is a demo version showing text extraction.\n"
            f"For full TTS conversion, use the local version from GitHub."
        )
        
        return output_filename, status_message
        
    except Exception as e:
        return None, f"❌ Error: {str(e)}"

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
    with gr.Blocks(title="Audiobook Converter Demo") as app:
        gr.HTML("""
        <div style="text-align: center; padding: 20px;">
            <h1>📚 Audiobook Converter - Demo</h1>
            <p>Text extraction demo from PDF and EPUB books</p>
            <p><em>🚧 This is a simplified demo version showing text extraction capabilities</em></p>
            <p><strong>For full TTS conversion, visit our <a href="https://github.com/LeonardoPizzoquero/audiobook-converter" target="_blank">GitHub repository</a></strong></p>
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
                    value="🇧🇷 Brazilian Portuguese",
                    label="🌍 Select Language",
                    info="Choose the language for narration"
                )
                
                narrator_input = gr.Dropdown(
                    choices=list(VOICE_CONFIG["🇧🇷 Brazilian Portuguese"]["voices"].keys()),
                    value="Dora (Female)",
                    label="🎭 Select Narrator",
                    info="Choose the voice (for full version)"
                )
                
                convert_btn = gr.Button(
                    "📝 Extract Text", 
                    variant="primary",
                    size="lg"
                )
            
            with gr.Column(scale=1):
                status_output = gr.Textbox(
                    label="📋 Processing Status",
                    lines=10,
                    interactive=False
                )
                
                download_output = gr.File(
                    label="📥 Download Extracted Text",
                    visible=True
                )
        
        gr.HTML("""
        <div style="margin-top: 20px; padding: 15px; background-color: #e3f2fd; border-radius: 10px;">
            <h3 style="margin-top: 0;">📌 About This Demo:</h3>
            <ul style="margin-bottom: 0;">
                <li>📄 <strong>Text Extraction:</strong> Extracts clean text from PDF and EPUB files</li>
                <li>📚 <strong>Format Support:</strong> Works with both PDF and EPUB formats</li>
                <li>🎭 <strong>Voice Preview:</strong> Shows available voices (TTS in full version only)</li>
                <li>🔧 <strong>Full Version:</strong> Complete TTS conversion available on <a href="https://github.com/LeonardoPizzoquero/audiobook-converter" target="_blank">GitHub</a></li>
                <li>🚀 <strong>Local Setup:</strong> Clone the repo and run locally for full audiobook generation</li>
            </ul>
        </div>
        """)
        
        language_input.change(
            fn=update_narrator_choices,
            inputs=[language_input],
            outputs=[narrator_input]
        )
        
        convert_btn.click(
            fn=process_book,
            inputs=[file_input, language_input, narrator_input],
            outputs=[download_output, status_output],
            show_progress="full"
        )
    
    return app

if __name__ == "__main__":
    app = create_interface()
    app.launch()