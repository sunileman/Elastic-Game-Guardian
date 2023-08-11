import openai
import time
import utils.es_config
from utils import es_config


def get_embedding(input_text):
    response = openai.Embedding.create(
        input=input_text,
        engine="ada-002",
        max_tokens=25
    )
    #print (input_text)

    embeddings = response['data'][0]['embedding']
    print(embeddings)
    time.sleep(es_config.rate_throttle)
    return embeddings
