import PyPDF2
import re
import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup
import gc

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
        print(f"Error reading PDF: {e}")
        return None
    return full_text

def extract_text_epub(epub_path):
    """Extract text from EPUB with basic optimization."""
    full_text = ""
    try:
        book = epub.read_epub(epub_path)
        items = list(book.get_items_of_type(ebooklib.ITEM_DOCUMENT))
        
        for item in items:
            try:
                content = item.get_content()
                soup = BeautifulSoup(content, 'html.parser')
                
                # Remove scripts, styles, and other non-content elements
                for script in soup(["script", "style"]):
                    script.decompose()
                
                text = soup.get_text()
                if text:
                    full_text += text + "\n"
                    
            except Exception as e:
                print(f"Error processing EPUB item: {e}")
                continue
                
    except Exception as e:
        print(f"Error reading EPUB: {e}")
        return None
    return full_text

def clean_text(text):
    """Clean text efficiently."""
    if not text:
        return ""
    
    text = re.sub(r'\n+', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^\w\s\.\,\!\?\;\:\-\(\)\"\']+', ' ', text)
    return text.strip()

def split_text_into_chunks(text, chunk_size=300):
    """Split text into chunks."""
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size):
        chunk = ' '.join(words[i:i+chunk_size])
        chunks.append(chunk)
    return chunks