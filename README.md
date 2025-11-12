# 📚 PDF/EPUB to Audiobook Converter# PDF/EPUB to Audiobook Converter# 📚 Audiobook Converter



Convert your PDF and EPUB books into high-quality audiobooks using AI voices in multiple languages.



## ✨ FeaturesEste projeto converte arquivos PDF e EPUB em audiolivros usando vozes de IA em múltiplos idiomas.Convert your PDF and EPUB books into high-quality audiobooks using AI voices in multiple languages.



- **📖 Multiple Formats**: Support for PDF and EPUB files

- **🌍 Multilingual**: 9 languages with 40+ different voices

- **🎵 High Quality**: 24kHz WAV output## 📋 Duas Versões Disponíveis## ✨ Features

- **⚡ Fast Processing**: Parallel audio generation

- **🎭 Voice Variety**: Male and female voices for each language

- **🔧 Easy to Use**: Web interface powered by Gradio

### 🎯 Versão Completa (Local) - `app.py`- **📖 Multiple Formats**: Support for PDF and EPUB files

## 🌍 Supported Languages & Voices

- **Funcionalidade completa** com conversão em audiolivro- **🌍 Multilingual**: 9 languages with 40+ voices

### 🇧🇷 Brazilian Portuguese (Default)

- **3 voices**: Dora (Female), Alex (Male), Santa (Male)- Suporte para 9 idiomas e 40+ vozes- **🎵 High Quality**: 24kHz WAV output



### 🇺🇸 American English  - Processamento paralelo otimizado- **⚡ Fast Processing**: Parallel audio generation

- **20 voices**: Heart⭐, Bella, Nicole, Alloy, Aoede, Jessica, Kore, Nova, River, Sarah, Sky (Female)

- Adam, Echo, Eric, Fenrir, Liam, Michael, Onyx, Puck, Santa (Male)- Execução local com todas as dependências- **🎭 Voice Variety**: Male and female voices for each language



### 🇬🇧 British English- **🔧 Easy to Use**: Web interface powered by Gradio

- **8 voices**: Alice, Emma, Isabella, Lily (Female) | Daniel, Fable, George, Lewis (Male)

### 🌐 Versão Demo (Online) - `app_demo.py`

### 🇪🇸 Spanish

- **3 voices**: Dora (Female) | Alex, Santa (Male)- **Demonstração simplificada** para deploy na nuvem## 🌍 Supported Languages & Voices



### 🇫🇷 French- Extração de texto apenas (sem síntese de áudio)

- **1 voice**: Siwis (Female)

- Compatível com Hugging Face Spaces### 🇧🇷 Brazilian Portuguese (Default)

### 🇮🇳 Hindi

- **4 voices**: Alpha, Beta (Female) | Omega, Psi (Male)- Dependências reduzidas- **3 voices**: Dora (Female), Alex (Male), Santa (Male)



### 🇮🇹 Italian

- **2 voices**: Sara (Female) | Nicola (Male)

## 🚀 Características da Versão Completa### 🇺🇸 American English  

### 🇯🇵 Japanese

- **5 voices**: Alpha, Gongitsune, Nezumi, Tebukuro (Female) | Kumo (Male)- **20 voices**: Heart⭐, Bella, Nicole, Alloy, Aoede, Jessica, Kore, Nova, River, Sarah, Sky (Female)



### 🇨🇳 Mandarin Chinese- Suporte para arquivos PDF e EPUB- Adam, Echo, Eric, Fenrir, Liam, Michael, Onyx, Puck, Santa (Male)

- **8 voices**: Xiaobei, Xiaoni, Xiaoxiao, Xiaoyi (Female) | Yunjian, Yunxi, Yunxia, Yunyang (Male)

- Interface web intuitiva com Gradio

## 🚀 Installation

- Processamento paralelo para maior velocidade### 🇬🇧 British English

### Prerequisites

- Suporte para 9 idiomas: Português (BR), Inglês (US/UK), Espanhol, Francês, Hindi, Italiano, Japonês, Chinês- **8 voices**: Alice, Emma, Isabella, Lily (Female) | Daniel, Fable, George, Lewis (Male)

- Python 3.8 or higher

- One of: pip + venv, Conda, or UV package manager- Mais de 40 vozes diferentes disponíveis



### Option 1: Using UV (Recommended)- Geração de audiolivros em alta qualidade (24kHz)### 🇪🇸 Spanish



1. **Clone the repository**- **3 voices**: Dora (Female) | Alex, Santa (Male)

```bash

git clone https://github.com/LeonardoPizzoquero/audiobook-converter.git## 📦 Instalação

cd audiobook-converter

```### 🇫🇷 French



2. **Install UV if you don't have it**### Versão Completa (Local)- **1 voice**: Siwis (Female)

```bash

curl -LsSf https://astral.sh/uv/install.sh | sh

```

#### Requisitos### 🇮🇳 Hindi

3. **Install dependencies**

```bash- Python 3.8+- **4 voices**: Alpha, Beta (Female) | Omega, Psi (Male)

uv sync

```- pip ou uv (recomendado)



4. **Run the application**### 🇮🇹 Italian

```bash

uv run app.py#### Usando uv (recomendado)- **2 voices**: Sara (Female) | Nicola (Male)

```

```bash

### Option 2: Using pip + venv

# Instalar uv se não tiver### 🇯🇵 Japanese

1. **Clone the repository**

```bashcurl -LsSf https://astral.sh/uv/install.sh | sh- **5 voices**: Alpha, Gongitsune, Nezumi, Tebukuro (Female) | Kumo (Male)

git clone https://github.com/LeonardoPizzoquero/audiobook-converter.git

cd audiobook-converter

```

# Instalar dependências### 🇨🇳 Mandarin Chinese

2. **Create and activate virtual environment**

```bashuv sync- **8 voices**: Xiaobei, Xiaoni, Xiaoxiao, Xiaoyi (Female) | Yunjian, Yunxi, Yunxia, Yunyang (Male)

python -m venv .venv

```

# On Linux/Mac:

source .venv/bin/activate## 🚀 Quick Start



# On Windows:#### Usando pip

.venv\Scripts\activate

``````bash### Prerequisites



3. **Install dependencies**pip install -r requirements.txt

```bash

pip install -r requirements.txt```- Python 3.8 or higher

```

- One of: pip + venv, Conda, or UV package manager

4. **Run the application**

```bash#### Execução

python app.py

``````bash### Installation



### Option 3: Using Condapython app.py



1. **Clone the repository**# ou#### Option 1: Using pip + venv (Standard)

```bash

git clone https://github.com/LeonardoPizzoquero/audiobook-converter.gituv run app.py

cd audiobook-converter

``````1. **Clone the repository**



2. **Create conda environment**```bash

```bash

conda create -n audiobook python=3.11### Versão Demo (Online)git clone https://github.com/LeonardoPizzoquero/audiobook-converter.git

conda activate audiobook

```cd audiobook-converter



3. **Install dependencies**Para deploy no Hugging Face Spaces:```

```bash

pip install -r requirements.txt1. Copie apenas os arquivos: `app_demo.py`, `requirements_demo.txt`, `text_processor.py`

```

2. Renomeie `app_demo.py` para `app.py`2. **Create and activate virtual environment**

4. **Run the application**

```bash3. Renomeie `requirements_demo.txt` para `requirements.txt````bash

python app.py

```4. Faça upload para o Hugging Face Spacespython -m venv .venv



## 💻 How to Use



1. **Start the application** following the installation steps above## 💻 Como usar# On Linux/Mac:

2. **Open your browser** and go to `http://localhost:7860`

3. **Upload** a PDF or EPUB filesource .venv/bin/activate

4. **Select the language** you want

5. **Choose the narrator voice**### Versão Local Completa

6. **Click "Convert to Audiobook"**

7. **Wait for processing** (may take a few minutes depending on file size)1. Execute `python app.py`# On Windows:

8. **Download** the resulting audio file

2. Abra `http://localhost:7860`.venv\Scripts\activate

## 📁 Project Structure

3. Faça upload de um arquivo PDF ou EPUB```

```

├── app.py                # 🎯 Main application4. Selecione o idioma e voz

├── voices.py             # 🎭 Voice and language configuration

├── text_processor.py     # 📄 PDF and EPUB text extraction5. Clique em "Converter para Audiolivro"3. **Install dependencies**

├── audio_processor.py    # 🎵 Text to audio conversion

├── requirements.txt      # 📦 Project dependencies6. Aguarde o processamento```bash

├── pyproject.toml        # ⚙️ Project configuration

└── README.md            # 📖 This file7. Faça download do audiolivropip install -r requirements.txt

```

```

## ⚠️ Limitations

### Versão Demo Online

- **Text-based PDFs**: Works best with PDFs containing selectable text

- **Scanned PDFs**: Does not support PDFs that are just images (requires OCR)1. Faça upload de um arquivo PDF ou EPUB#### Option 2: Using Conda

- **Large files**: May take time to process and require significant RAM

- **Text quality**: Audio quality depends on the quality of extracted text2. Visualize o texto extraído



## 🔧 Main Dependencies3. Para conversão completa, use a versão local1. **Clone the repository**



- **kokoro-onnx**: Voice synthesis using Kokoro TTS models```bash

- **gradio**: Web interface for interaction

- **PyPDF2**: PDF reading and text extraction## 📁 Estrutura do Projetogit clone https://github.com/LeonardoPizzoquero/audiobook-converter.git

- **ebooklib**: EPUB file processing

- **beautifulsoup4**: HTML parsing for EPUBscd audiobook-converter

- **numpy**: Numerical processing for audio

- **soundfile**: Audio file manipulation``````



## 🐛 Troubleshooting├── app.py                 # 🎯 Aplicação completa (local)



### Issue: Error installing dependencies├── app_demo.py           # 🌐 Versão demo (cloud)2. **Create and activate conda environment**

**Solution**: Make sure you have Python 3.8+ and try using clean virtual environments.

├── voices.py             # Configuração de vozes```bash

### Issue: Audio cut off or poor quality

**Solution**: Check if text was extracted correctly. Scanned PDFs may have extraction issues.├── text_processor.py     # Extração de texto# Create environment with Python 3.11



### Issue: Very slow processing├── audio_processor.py    # Conversão em áudioconda create -n audiobook-converter python=3.11

**Solution**: Parallel processing is already optimized. For very large files, consider splitting into smaller parts.

├── requirements.txt      # Dependências completas

### Issue: Interface doesn't open in browser

**Solution**: Check if port 7860 is free or change the port in the code.└── requirements_demo.txt # Dependências da demo# Activate environment



## 📄 License```conda activate audiobook-converter



MIT License - See the `LICENSE` file for details.```



## 🤝 Contributing## 🌍 Idiomas e Vozes Suportadas (Versão Completa)



Contributions are welcome! Feel free to:3. **Install dependencies**



- Report bugs### 🇧🇷 Português Brasileiro```bash

- Suggest new features

- Improve documentation- Dora (Feminina), Alex (Masculina), Santa (Masculina)# Install pip packages in conda environment

- Add support for new file formats

pip install -r requirements.txt

## ⭐ Support

### 🇺🇸 Inglês Americano  

If this project was helpful to you, consider giving it a star on GitHub!
- 20 vozes: Heart, Bella, Nicole, Alloy, Aoede, Jessica, Kore, Nova, River, Sarah, Sky (Femininas)# Alternative: Install available packages via conda first

- Adam, Echo, Eric, Fenrir, Liam, Michael, Onyx, Puck, Santa (Masculinas)conda install numpy soundfile

pip install gradio kokoro-tts PyPDF2 ebooklib beautifulsoup4 tqdm

### 🇬🇧 Inglês Britânico```

- 8 vozes: Alice, Emma, Isabella, Lily (Femininas) | Daniel, Fable, George, Lewis (Masculinas)

#### Option 3: Using UV (Fast Package Manager)

### 🇪🇸 Espanhol

- Dora (Feminina) | Alex, Santa (Masculinas)1. **Install UV** (if not already installed)

```bash

### 🇫🇷 Francês# On Linux/Mac:

- Siwis (Feminina)curl -LsSf https://astral.sh/uv/install.sh | sh



### 🇮🇳 Hindi# On Windows (PowerShell):

- Alpha, Beta (Femininas) | Omega, Psi (Masculinas)powershell -c "irm https://astral.sh/uv/install.ps1 | iex"

```

### 🇮🇹 Italiano

- Sara (Feminina) | Nicola (Masculino)2. **Clone and setup project**

```bash

### 🇯🇵 Japonêsgit clone https://github.com/LeonardoPizzoquero/audiobook-converter.git

- Alpha, Gongitsune, Nezumi, Tebukuro (Femininas) | Kumo (Masculino)cd audiobook-converter



### 🇨🇳 Chinês Mandarim# Create virtual environment and install dependencies in one command

- Xiaobei, Xiaoni, Xiaoxiao, Xiaoyi (Femininas) | Yunjian, Yunxi, Yunxia, Yunyang (Masculinas)uv sync



## ⚠️ Limitações# Or manually:

uv venv

### Versão Completasource .venv/bin/activate  # Linux/Mac

- Requer instalação local das dependências Kokoro TTS# .venv\Scripts\activate   # Windows

- Funciona melhor com PDFs baseados em textouv pip install -r requirements.txt

- PDFs digitalizados (imagens) não são suportados```

- Requer bastante memória RAM para arquivos grandes

### Usage

### Versão Demo

- Apenas extração de texto (sem síntese de áudio)#### Running with pip + venv

- Demonstra a funcionalidade de processamento de texto1. **Activate environment and start the application**

```bash

## 🔧 Dependências Principaissource .venv/bin/activate  # Linux/Mac

# .venv\Scripts\activate   # Windows

### Versão Completapython main.py

- kokoro-onnx (síntese de voz)```

- gradio (interface web)

- PyPDF2 (leitura de PDF)#### Running with Conda

- ebooklib (leitura de EPUB)1. **Activate environment and start the application**

```bash

### Versão Democonda activate audiobook-converter

- gradio (interface web)python main.py

- PyPDF2 (leitura de PDF)```

- ebooklib (leitura de EPUB)

- beautifulsoup4 (processamento HTML)#### Running with UV

1. **Start the application**

## 📄 Licença```bash

# If using uv sync:

MIT Licenseuv run python main.py

# If using manual venv:
source .venv/bin/activate  # Linux/Mac
# .venv\Scripts\activate   # Windows
python main.py
```

#### Using the Application

1. **The app will start on port 7860**
   - You'll see output like: `Running on local URL:  http://127.0.0.1:7860`
   - Open your browser to: `http://localhost:7860`

2. **Convert your book**
   - Upload your PDF or EPUB file
   - Select language and narrator  
   - Click "Convert to Audiobook"
   - Wait for processing (progress will be shown)
   - Download the generated WAV file

3. **Stop the application**
   - Press `Ctrl+C` in the terminal to stop the server

## 📁 Project Structure

```
audiobook-converter/
├── main.py      # Main Gradio application
├── voices.py              # Voice and language configuration
├── text_processor.py      # PDF/EPUB text extraction
├── audio_processor.py     # Audio generation and processing
├── requirements.txt       # Python dependencies
├── README.md             # This file
└── main.py              # Original script (legacy)
```

## 🛠️ Configuration

### Adjusting Performance

You can modify processing parameters in `audio_processor.py`:

- `max_workers`: Number of parallel threads (default: 4)
- `chunk_size`: Text chunk size for processing (default: 200 words)
- `sample_rate`: Audio output sample rate (default: 24000 Hz)

### Adding Custom Voices

To add new voices, update the `VOICE_CONFIG` in `voices.py` following the existing pattern.

##  Requirements

- **gradio**: Web interface framework
- **kokoro-tts**: AI text-to-speech engine
- **soundfile**: Audio file processing
- **numpy**: Numerical computations
- **PyPDF2**: PDF text extraction
- **ebooklib**: EPUB text extraction
- **beautifulsoup4**: HTML parsing for EPUB
- **tqdm**: Progress bars

## 💡 Quick Start Commands

| Package Manager | Setup | Run App (Port 7860) |
|----------------|-------|---------------------|
| **pip + venv** | `python -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt` | `python main.py` |
| **Conda** | `conda create -n audiobook-converter python=3.11 && conda activate audiobook-converter && pip install -r requirements.txt` | `python main.py` |
| **UV** | `uv sync` | `uv run python main.py` |

> 🌐 **Access the app**: Open your browser to `http://localhost:7860` after running any of the commands above.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- **Kokoro TTS**: For providing the high-quality AI voices
- **Gradio**: For the excellent web interface framework
- **Contributors**: Thank you to all contributors who help improve this project

## 🐛 Troubleshooting

### Common Issues

**Installation Problems:**
- Ensure you're using Python 3.8+
- Try updating pip: `pip install --upgrade pip`
- Use virtual environment to avoid conflicts

**Memory Issues:**
- Reduce `max_workers` in audio_processor.py
- Increase `chunk_size` for longer text segments

**Audio Quality:**
- Ensure input text is clean and well-formatted
- Try different voices for better results
- Check that the selected language matches your text

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Issues](link-to-issues) page
2. Create a new issue with detailed information
3. Include error messages and system information

---

**Made with ❤️ for the audiobook community**