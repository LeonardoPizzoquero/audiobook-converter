# 📚 Audiobook Converter

Convert your PDF and EPUB books into audiobooks with multilingual AI voices powered by Kokoro TTS!

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Gradio](https://img.shields.io/badge/UI-Gradio-orange.svg)](https://gradio.app/)

## ✨ Features

- **📖 Multiple formats**: Support for PDF and EPUB files
- **🌍 9 languages**: Brazilian Portuguese, American English, British English, Spanish, French, Hindi, Italian, Japanese, and Mandarin Chinese
- **🎭 40+ voices**: Multiple male and female voices for each language
- **🖥️ Web interface**: Easy-to-use Gradio web interface
- **⚡ Parallel processing**: Fast audio generation with multi-threading
- **🎵 High quality**: 24kHz WAV output files

## 🌐 Supported Languages & Voices

| Language | Code | Female Voices | Male Voices | Total |
|----------|------|---------------|-------------|-------|
| 🇧🇷 Brazilian Portuguese | `pt-BR` | 1 | 2 | **3** |
| 🇺🇸 American English | `en-US` | 11 | 9 | **20** |
| 🇬🇧 British English | `en-GB` | 4 | 4 | **8** |
| 🇪🇸 Spanish | `es` | 1 | 2 | **3** |
| 🇫🇷 French | `fr` | 1 | 0 | **1** |
| 🇮🇳 Hindi | `hi` | 2 | 2 | **4** |
| 🇮🇹 Italian | `it` | 1 | 1 | **2** |
| 🇯🇵 Japanese | `ja` | 4 | 1 | **5** |
| 🇨🇳 Mandarin Chinese | `zh` | 4 | 4 | **8** |

**Total: 9 languages with 54 unique voices**

## 🚀 Installation

### Option 1: Using uv (Recommended)

```bash
# Clone the repository
git clone https://github.com/LeonardoPizzoquero/audiobook-converter.git
cd audiobook-converter

# Install uv if you haven't already
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install dependencies with uv
uv sync
```

### Option 2: Using conda

```bash
# Clone the repository
git clone https://github.com/LeonardoPizzoquero/audiobook-converter.git
cd audiobook-converter

# Create conda environment
conda create -n audiobook python=3.11
conda activate audiobook

# Install dependencies
pip install -r requirements.txt
```

### Option 3: Using pip

```bash
# Clone the repository
git clone https://github.com/LeonardoPizzoquero/audiobook-converter.git
cd audiobook-converter

# Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## 🎮 Usage

### Running the Web Interface

#### With uv:
```bash
uv run python app.py
```

#### With conda:
```bash
conda activate audiobook
python app.py
```

#### With pip/venv:
```bash
# If using virtual environment, activate it first
source venv/bin/activate  # On Windows: venv\Scripts\activate
python app.py
```

### Using the Interface

1. **📁 Upload your book**: Select a PDF or EPUB file
2. **🌍 Choose language**: Select from 9 available languages
3. **🎭 Pick a voice**: Choose from multiple narrator options
4. **🎵 Convert**: Click "Convert to Audiobook" and wait for processing
5. **📥 Download**: Get your high-quality WAV audiobook file

## 📋 Requirements

- **Python**: 3.11 or higher
- **Memory**: At least 4GB RAM recommended
- **Storage**: Additional space for output files
- **Internet**: Required for initial model downloads

## 💡 Tips for Best Results

- **📄 PDF files**: Works best with text-based PDFs (not scanned images)
- **📚 EPUB files**: Full support for all EPUB formats
- **🎭 Voice selection**: Try different voices to find your preferred style
- **⏰ Processing time**: 
  - Small books (~50 pages): 2-5 minutes
  - Medium books (~200 pages): 5-10 minutes
  - Large books (500+ pages): 15-30 minutes
- **🎵 Output**: High-quality 24kHz WAV files ready for any audio player

## 🛠️ Technical Details

- **TTS Engine**: Kokoro TTS for natural-sounding voices
- **Text Processing**: Automatic cleaning and chunking for optimal audio generation
- **Audio Format**: 24kHz WAV files
- **Parallel Processing**: Multi-threaded audio generation for faster processing
- **Web Framework**: Gradio for the user interface

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 🐛 Issues

If you encounter any problems or have suggestions, please [open an issue](https://github.com/LeonardoPizzoquero/audiobook-converter/issues) on GitHub.

## ⭐ Acknowledgments

- [Kokoro TTS](https://github.com/jnoordsij/kokoro) for the amazing text-to-speech engine
- [Gradio](https://gradio.app/) for the web interface framework
- All contributors and users who help improve this project

---

**Made with ❤️ by [Leonardo Pizzoquero](https://github.com/LeonardoPizzoquero)**