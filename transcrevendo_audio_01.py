import openai
from dotenv import load_dotenv

load_dotenv()

client = openai.OpenAI()

def transcreve_audio(caminho_audio, language="pt", response_format="text"):
    with open(caminho_audio, "rb") as arquivo_audio:
        transcricao = client.audio.transcriptions.create(
            model="whisper-1",
            language=language,
            response_format=response_format,
            file=arquivo_audio
        )
    return transcricao

# response_format="srt" => É um formato de legenda
print(transcreve_audio("./audios/audio.mp3"))