import openai
from dotenv import load_dotenv

load_dotenv()
client = openai.OpenAI()

def chat_openai(
        mensagens,
        modelo='gpt-3.5-turbo-1106',
        temperatura=0,
        stream=False
    ):
    resposta = client.chat.completions.create(
        model=modelo,
        messages=mensagens,
        temperature=temperatura,
        stream=stream
    )
    return resposta.choices[0].message.content