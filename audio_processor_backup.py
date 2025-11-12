import numpy as np
import soundfile as sf
from kokoro import KPipeline
from concurrent.futures import ThreadPoolExecutor, as_completed
import gc

def process_audio_chunk(chunk_data, voice_code, lang_code):
    """Process a single audio chunk."""
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

def convert_chunks_to_audio_sequential(chunks, voice_code, lang_code, progress_callback=None, save_parts=False, output_base="temp_audio"):
    """Convert chunks to audio sequentially (for EPUBs) with optional part saving."""
    audio_parts = []
    part_files = []
    
    try:
        pipeline = KPipeline(lang_code=lang_code, repo_id='hexgrad/Kokoro-82M')
        
        for i, chunk in enumerate(chunks):
            try:
                local_audio_chunks = []
                generator = pipeline(chunk, voice=voice_code)
                
                for gs, ps, audio in generator:
                    # Converter para numpy array se necessário
                    if hasattr(audio, 'numpy'):
                        audio = audio.numpy()
                    elif hasattr(audio, 'cpu'):
                        audio = audio.cpu().numpy()
                    
                    if audio is not None and len(audio) > 0:
                        local_audio_chunks.append(audio)
                
                if local_audio_chunks:
                    chunk_audio = np.concatenate(local_audio_chunks, axis=0)
                    
                    if save_parts and i % 50 == 0 and audio_parts:
                        part_filename = f"{output_base}_part_{i//50:03d}.wav"
                        combined_part = np.concatenate(audio_parts, axis=0)
                        sf.write(part_filename, combined_part, samplerate=24000)
                        part_files.append(part_filename)
                        audio_parts = []
                        print(f"Saved audio part {len(part_files)} ({i} chunks processed)")
                    
                    audio_parts.append(chunk_audio)
                
                if progress_callback:
                    progress_callback(i + 1, len(chunks))
                    
            except Exception as e:
                print(f"Error processing chunk {i}: {e}")
                continue
        
        # Salvar parte final se usando save_parts
        if save_parts and audio_parts:
            part_filename = f"{output_base}_part_{len(part_files):03d}.wav"
            combined_part = np.concatenate(audio_parts, axis=0)
            sf.write(part_filename, combined_part, samplerate=24000)
            part_files.append(part_filename)
            print(f"Saved final audio part {len(part_files)}")
            return part_files
        
        # Retornar áudio concatenado
        if audio_parts:
            return np.concatenate(audio_parts, axis=0)
        else:
            return None
            
    except Exception as e:
        print(f"Error in sequential processing: {e}")
        return None
                            part_files.append(part_filename)
                            audio_parts = []
                            print(f"Saved audio part {len(part_files)} ({i} chunks processed)")
                    
                    audio_parts.append(chunk_audio)
                
                if progress_callback:
                    progress_callback(i + 1, len(chunks))
                    
            except Exception as e:
                print(f"Error processing chunk {i}: {e}")
                continue
        
        if save_parts and audio_parts:
            part_filename = f"{output_base}_part_{len(part_files):03d}.wav"
            combined_part = np.concatenate(audio_parts, axis=0)
            sf.write(part_filename, combined_part, samplerate=24000)
            part_files.append(part_filename)
            print(f"Saved final audio part {len(part_files)}")
            return part_files
        
        if audio_parts:
            return np.concatenate(audio_parts, axis=0)
        else:
            return None
            
    except Exception as e:
        print(f"Error in sequential processing: {e}")
        return None

def convert_chunks_to_audio(chunks, voice_code, lang_code, progress_callback=None, max_workers=2, sequential=False):
    """Convert chunks to audio with parallel or sequential processing."""
    if sequential:
        return convert_chunks_to_audio_sequential(chunks, voice_code, lang_code, progress_callback)
    
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
    """Concatenate audio results efficiently."""
    if audio_results is None:
        return None
    
    # Se já é um array numpy (processamento sequencial), retorna diretamente
    if isinstance(audio_results, np.ndarray):
        return audio_results
    
    # Se é um dicionário (processamento paralelo), processa como antes
    if isinstance(audio_results, dict):
        if not audio_results:
            return None
            
        ordered_chunks = []
        for i in sorted(audio_results.keys()):
            if i in audio_results and audio_results[i] is not None:
                ordered_chunks.append(audio_results[i])
        
        if not ordered_chunks:
            return None
        
        return np.concatenate(ordered_chunks, axis=0)
    
    # Se é uma lista (caso especial)
    if isinstance(audio_results, list):
        if not audio_results:
            return None
        return np.concatenate(audio_results, axis=0)
    
    return None

def save_audio(audio_data, output_file, sample_rate=24000):
    sf.write(output_file, audio_data, samplerate=sample_rate)
    duration = len(audio_data) / sample_rate
    return duration