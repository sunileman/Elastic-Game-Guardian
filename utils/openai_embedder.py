import openai
import time
import utils.es_config
from utils import es_config
from variables import openai_embedding_deployment_name


def get_embedding(input_text):
    response = openai.Embedding.create(
        input=input_text,
        engine=openai_embedding_deployment_name,
        max_tokens=25
    )
    #print (input_text)

    embeddings = response['data'][0]['embedding']
    print(embeddings)
    time.sleep(es_config.rate_throttle)
    return embeddings
