# 📚 Audiobook Converter

Convert your PDF and EPUB books into high-quality audiobooks using AI voices in multiple languages.

## ✨ Features

- **📖 Multiple Formats**: Support for PDF and EPUB files
- **🌍 Multilingual**: 9 languages with 40+ voices
- **🎵 High Quality**: 24kHz WAV output
- **⚡ Fast Processing**: Parallel audio generation
- **🎭 Voice Variety**: Male and female voices for each language
- **🔧 Easy to Use**: Web interface powered by Gradio

## 🌍 Supported Languages & Voices

### 🇧🇷 Brazilian Portuguese (Default)
- **3 voices**: Dora (Female), Alex (Male), Santa (Male)

### 🇺🇸 American English  
- **20 voices**: Heart⭐, Bella, Nicole, Alloy, Aoede, Jessica, Kore, Nova, River, Sarah, Sky (Female)
- Adam, Echo, Eric, Fenrir, Liam, Michael, Onyx, Puck, Santa (Male)

### 🇬🇧 British English
- **8 voices**: Alice, Emma, Isabella, Lily (Female) | Daniel, Fable, George, Lewis (Male)

### 🇪🇸 Spanish
- **3 voices**: Dora (Female) | Alex, Santa (Male)

### 🇫🇷 French
- **1 voice**: Siwis (Female)

### 🇮🇳 Hindi
- **4 voices**: Alpha, Beta (Female) | Omega, Psi (Male)

### 🇮🇹 Italian
- **2 voices**: Sara (Female) | Nicola (Male)

### 🇯🇵 Japanese
- **5 voices**: Alpha, Gongitsune, Nezumi, Tebukuro (Female) | Kumo (Male)

### 🇨🇳 Mandarin Chinese
- **8 voices**: Xiaobei, Xiaoni, Xiaoxiao, Xiaoyi (Female) | Yunjian, Yunxi, Yunxia, Yunyang (Male)

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- One of: pip + venv, Conda, or UV package manager

### Installation

#### Option 1: Using pip + venv (Standard)

1. **Clone the repository**
```bash
git clone https://github.com/LeonardoPizzoquero/audiobook-converter.git
cd audiobook-converter
```

2. **Create and activate virtual environment**
```bash
python -m venv .venv

# On Linux/Mac:
source .venv/bin/activate

# On Windows:
.venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

#### Option 2: Using Conda

1. **Clone the repository**
```bash
git clone https://github.com/LeonardoPizzoquero/audiobook-converter.git
cd audiobook-converter
```

2. **Create and activate conda environment**
```bash
# Create environment with Python 3.11
conda create -n audiobook-converter python=3.11

# Activate environment
conda activate audiobook-converter
```

3. **Install dependencies**
```bash
# Install pip packages in conda environment
pip install -r requirements.txt

# Alternative: Install available packages via conda first
conda install numpy soundfile
pip install gradio kokoro-tts PyPDF2 ebooklib beautifulsoup4 tqdm
```

#### Option 3: Using UV (Fast Package Manager)

1. **Install UV** (if not already installed)
```bash
# On Linux/Mac:
curl -LsSf https://astral.sh/uv/install.sh | sh

# On Windows (PowerShell):
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

2. **Clone and setup project**
```bash
git clone https://github.com/LeonardoPizzoquero/audiobook-converter.git
cd audiobook-converter

# Create virtual environment and install dependencies in one command
uv sync

# Or manually:
uv venv
source .venv/bin/activate  # Linux/Mac
# .venv\Scripts\activate   # Windows
uv pip install -r requirements.txt
```

### Usage

#### Running with pip + venv
1. **Activate environment and start the application**
```bash
source .venv/bin/activate  # Linux/Mac
# .venv\Scripts\activate   # Windows
python main.py
```

#### Running with Conda
1. **Activate environment and start the application**
```bash
conda activate audiobook-converter
python main.py
```

#### Running with UV
1. **Start the application**
```bash
# If using uv sync:
uv run python main.py

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