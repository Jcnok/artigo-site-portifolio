import os
import base64
from openai import AzureOpenAI
from dotenv import load_dotenv

load_dotenv()

endpoint = os.getenv("AZURE_OPENAI_ENDPOINT", "https://openai-dio-boot-east1.openai.azure.com/")
deployment = os.getenv("DEPLOYMENT_NAME", "gpt-4o-mini")
subscription_key = os.getenv("AZURE_OPENAI_API_KEY", "REPLACE_WITH_YOUR_KEY_VALUE_HERE")

# Inicializar o cliente OpenAI do Azure com autenticação baseada em chave
client = AzureOpenAI(
    azure_endpoint=endpoint,
    api_key=subscription_key,
    api_version="2025-01-01-preview",
)

# Preparar o prompt de chat
chat_prompt = [
    {
        "role": "system",
        "content": [
            {
                "type": "text",
                "text": "Você é um assistente de IA que ajuda as pessoas a encontrar informações."
            }
        ]
    },
    {
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": "Quem descobriu o Brasil?"
            }
        ]
    }
]

# Gerar a conclusão
completion = client.chat.completions.create(
    model=deployment,
    messages=chat_prompt,
    max_tokens=800,
    temperature=0.7,
    top_p=0.95,
    frequency_penalty=0,
    presence_penalty=0,
    stop=None,
    stream=False
)

print(completion.model_dump_json())
