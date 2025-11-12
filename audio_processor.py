import numpy as np
import soundfile as sf
from kokoro import KPipeline
from concurrent.futures import ThreadPoolExecutor, as_completed

def process_audio_chunk(chunk_data, voice_code, lang_code):
    chunk_text, chunk_id = chunk_data
    try:
        pipeline = KPipeline(lang_code=lang_code, repo_id='hexgrad/Kokoro-82M')
        local_audio_chunks = []
        generator = pipeline(chunk_text, voice=voice_code)
        
        for gs, ps, audio in generator:
            local_audio_chunks.append(audio)
        
        if local_audio_chunks:
            complete_audio_chunk = np.concatenate(local_audio_chunks, axis=0)
            return chunk_id, complete_audio_chunk
        else:
            return chunk_id, None
    except Exception as e:
        print(f"Error processing chunk {chunk_id}: {e}")
        return chunk_id, None

def convert_chunks_to_audio(chunks, voice_code, lang_code, progress_callback=None, max_workers=4):
    chunk_data = [(chunk, i) for i, chunk in enumerate(chunks)]
    audio_results = {}
    
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_chunk = {
            executor.submit(process_audio_chunk, data, voice_code, lang_code): data[1] 
            for data in chunk_data
        }
        
        completed = 0
        total = len(chunks)
        
        for future in as_completed(future_to_chunk):
            chunk_id = future_to_chunk[future]
            try:
                result_id, audio_chunk = future.result()
                if audio_chunk is not None:
                    audio_results[result_id] = audio_chunk
                completed += 1
                if progress_callback:
                    progress_callback(completed, total)
            except Exception as e:
                print(f"Error in chunk {chunk_id}: {e}")
                completed += 1
    
    return audio_results

def concatenate_audio(audio_results):
    ordered_chunks = []
    for i in sorted(audio_results.keys()):
        if i in audio_results:
            ordered_chunks.append(audio_results[i])
    
    if not ordered_chunks:
        return None
    
    return np.concatenate(ordered_chunks, axis=0)

def save_audio(audio_data, output_file, sample_rate=24000):
    sf.write(output_file, audio_data, samplerate=sample_rate)
    duration = len(audio_data) / sample_rate
    return duration