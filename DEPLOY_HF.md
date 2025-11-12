# 🚀 Deploy no Hugging Face Spaces

## Passos para fazer o deploy:

### 1. Clone o repositório do Space
```bash
git clone https://huggingface.co/spaces/LeonardoP/audiobook-converter
cd audiobook-converter
```

### 2. Copie os arquivos necessários
Copie estes arquivos do seu projeto local:

```bash
# Aplicação principal (versão otimizada para HF)
cp /caminho/do/seu/projeto/app_hf.py ./app.py

# Módulos auxiliares
cp /caminho/do/seu/projeto/voices.py .
cp /caminho/do/seu/projeto/text_processor.py .
cp /caminho/do/seu/projeto/audio_processor.py .

# Dependências otimizadas para HF
cp /caminho/do/seu/projeto/requirements_hf.txt ./requirements.txt

# README para o Space
cp /caminho/do/seu/projeto/README_HF.md ./README.md
```

### 3. Faça commit e push
```bash
git add .
git commit -m "Add audiobook converter application"
git push
```

### 4. Aguarde o deploy
- O Space irá aparecer em: https://huggingface.co/spaces/LeonardoP/audiobook-converter
- O deploy leva alguns minutos
- Você verá logs em tempo real na página do Space

## 📋 Arquivos necessários no Space:

```
audiobook-converter/
├── app.py                    # Aplicação principal
├── voices.py                 # Configurações de vozes
├── text_processor.py         # Processamento de texto
├── audio_processor.py        # Processamento de áudio
├── requirements.txt          # Dependências Python
└── README.md                # Documentação do Space
```

## 💡 Configurações importantes:

1. **requirements.txt**: Use `requirements_spaces.txt` como base
2. **app.py**: Já está otimizado para Hugging Face
3. **README.md**: Use `README_HF.md` com metadata do Space

## 🔧 Troubleshooting:

- **Erro de dependências**: Verifique o requirements.txt
- **Timeout**: Reduza `max_workers` no audio_processor.py
- **Memória**: Aumente `chunk_size` no text_processor.py

## 🌐 URL final:
https://huggingface.co/spaces/LeonardoP/audiobook-converter