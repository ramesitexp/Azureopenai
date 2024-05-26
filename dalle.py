# Note: DALL-E 3 requires version 1.0.0 of the openai-python library or later
import os
from openai import AzureOpenAI
import json


endpoint='https://harsigenai.openai.azure.com/'
deployment='chatcompletion'
token_provider='a0acfb52a34249aca75662ce7bb7cfc3'

client = AzureOpenAI(
    api_version="2024-02-01",
    azure_endpoint="https://harsigenai.openai.azure.com/",
    api_key=token_provider,
)

result = client.images.generate(
    model="Dalle3", # the name of your DALL-E 3 deployment
    prompt="please provide dhoni actual image",
    n=1
)

image_url = json.loads(result.model_dump_json())['data'][0]['url']

print(image_url)