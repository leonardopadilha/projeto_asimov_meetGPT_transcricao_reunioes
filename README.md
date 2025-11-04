# MeetGPT – Transcrição de Reuniões 🎙️

Um Web App desenvolvido em Python para transcrição e análise de reuniões corporativas em tempo real. Este projeto permite capturar áudios de reuniões, convertê-los em texto e gerar resumos precisos usando a API da OpenAI.

## 📋 Sobre o Projeto

Este projeto foi desenvolvido com base no curso **MeetGPT – Transcrição de reuniões** da [Asimov Academy](https://hub.asimov.academy/projeto/meetgpt-transcricao-de-reunioes/).

A aplicação facilita a documentação de reuniões, garantindo que todos os detalhes e decisões importantes sejam registrados. Além disso, serve como base para criação de assistentes virtuais, sistemas de apoio a deficientes auditivos e outras inovações que utilizam processamento de linguagem natural.

## ✨ Funcionalidades

- 🎤 **Gravação de áudio em tempo real** via microfone do navegador
- 📝 **Transcrição automática** de áudio usando o modelo Whisper da OpenAI
- 📊 **Geração de resumos inteligentes** com os principais assuntos abordados
- ✅ **Extração de acordos e combinados** da reunião
- 💾 **Armazenamento de histórico** de reuniões com data e hora
- 🔍 **Visualização de transcrições** salvas anteriormente
- 📌 **Títulos personalizados** para cada reunião

## 🛠️ Tecnologias Utilizadas

- **Python** - Linguagem de programação principal
- **Streamlit** - Framework para criação da interface web
- **streamlit-webrtc** - Captura de áudio em tempo real do navegador
- **OpenAI API** - Modelos Whisper (transcrição) e GPT (resumos)
- **pydub** - Processamento de áudio
- **python-dotenv** - Gerenciamento de variáveis de ambiente

## 📦 Pré-requisitos

Antes de começar, certifique-se de ter instalado:

- Python 3.8 ou superior
- Conta na OpenAI com API Key
- Microfone funcional no seu computador

## 🚀 Instalação

1. Clone este repositório ou baixe os arquivos do projeto:

```bash
git clone <url-do-repositorio>
cd projeto
```

2. Crie um ambiente virtual (recomendado):

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Crie um arquivo `.env` na raiz do projeto e adicione sua API Key da OpenAI:

```env
OPENAI_API_KEY=sua-api-key-aqui
```

Para obter uma API Key:
- Acesse [https://platform.openai.com/api-keys](https://platform.openai.com/api-keys)
- Faça login ou crie uma conta
- Crie uma nova API Key
- Copie a chave e adicione no arquivo `.env`

## 🎯 Como Usar

1. Execute a aplicação Streamlit:

```bash
streamlit run transcrevendo_audio_07.py
```

2. Acesse a aplicação no navegador (geralmente em `http://localhost:8501`)

3. Na aba **"Gravar Reunião"**:
   - Clique em "Start" para iniciar a gravação
   - Comece a falar no microfone
   - A transcrição aparecerá em tempo real
   - Clique em "Stop" para finalizar a gravação

4. Na aba **"Ver transcrições salvas"**:
   - Selecione uma reunião da lista
   - Adicione um título personalizado (se necessário)
   - Visualize a transcrição completa
   - O resumo será gerado automaticamente

## 📁 Estrutura do Projeto

```
projeto/
│
├── arquivos/              # Pasta onde são salvos os arquivos das reuniões
│   └── YYYY_MM_DD_HH_MM_SS/
│       ├── audio.mp3      # Áudio completo da reunião
│       ├── audio_temp.mp3 # Áudio temporário (chunks)
│       ├── transcricao.txt # Transcrição completa
│       ├── resumo.txt     # Resumo gerado pelo GPT
│       └── titulo.txt     # Título da reunião
│
├── audios/                # Pasta para arquivos de áudio de teste
├── transcrevendo_audio_01.py  # Versão inicial (transcrição básica)
├── transcrevendo_audio_02.py  # Versões intermediárias
├── transcrevendo_audio_03.py
├── transcrevendo_audio_04.py
├── transcrevendo_audio_05.py
├── transcrevendo_audio_06.py
├── transcrevendo_audio_07.py  # Versão final (aplicação completa)
├── requirements.txt       # Dependências do projeto
├── ffmpeg.exe            # Utilitário de processamento de áudio
└── README.md             # Este arquivo
```

## 🔧 Configurações

### Formato de Transcrição

O projeto utiliza o modelo `whisper-1` da OpenAI com as seguintes configurações:
- Idioma: Português (`pt`)
- Formato de resposta: Texto (`text`)

### Modelo de Resumo

O resumo é gerado usando o modelo `gpt-3.5-turbo-1106` com um prompt personalizado que:
- Resume os principais assuntos (máximo 300 caracteres)
- Extrai todos os acordos e combinados
- Formata a saída de forma estruturada

## 📚 Recursos de Aprendizado

Este projeto foi baseado no curso da Asimov Academy e cobre os seguintes tópicos:

1. **Introdução à API da OpenAI**
   - Criação de conta e API Key
   - Transcrição de áudios com Whisper
   - Utilização do ChatGPT via API

2. **Desenvolvimento do Web App**
   - Estrutura do projeto
   - Captura de áudio via Streamlit
   - Geração de transcrição em tempo real
   - Visualização e armazenamento de reuniões
   - Geração automática de resumos

## ⚠️ Observações Importantes

- Certifique-se de ter créditos suficientes na sua conta OpenAI
- O modelo Whisper cobra por minuto de áudio processado
- A gravação funciona melhor em ambientes com pouco ruído
- O microfone precisa estar permitido pelo navegador

## 🤝 Contribuições

Este é um projeto educacional baseado em um curso. Sinta-se à vontade para:
- Fazer fork do projeto
- Sugerir melhorias
- Adicionar novas funcionalidades
- Reportar bugs

## 📄 Licença

Este projeto é para fins educacionais. Verifique os termos de uso da OpenAI ao utilizar a API.

## 🔗 Links Úteis

- [Curso Original - Asimov Academy](https://hub.asimov.academy/projeto/meetgpt-transcricao-de-reunioes/)
- [Documentação da OpenAI](https://platform.openai.com/docs)
- [Documentação do Streamlit](https://docs.streamlit.io/)
- [Streamlit WebRTC](https://github.com/whitphx/streamlit-webrtc)

## 📝 Notas

- Os arquivos `transcrevendo_audio_01.py` até `transcrevendo_audio_06.py` são versões intermediárias do desenvolvimento
- O arquivo `transcrevendo_audio_07.py` contém a versão final e completa da aplicação
- Execute `transcrevendo_audio_07.py` para usar a aplicação completa

---

Desenvolvido com ❤️ seguindo o curso da Asimov Academy

