# Import the required libraries
from elasticsearch import Elasticsearch, helpers
import requests
import json

from utils.es_config import index_name, settings, mappings, embedded_file_name, deleteExistingIndex
from utils.es_helper import create_es_client, manage_index
from variables import es_username, es_cloudid, es_password


def ingest_data_into_elastic():
    try:
        # Create Elasticsearch connection
        username = es_username
        password = es_password
        cloudid = es_cloudid

        # get es object
        es = create_es_client(username, password, cloudid)

        print(es.info())
    except Exception as e:
        return f"Connection failed: {e}"

    # Create index
    manage_index(es, index_name, settings, mappings, deleteExistingIndex)

    def generate_actions(url):
        response = requests.get(url)
        response.raise_for_status()

        for line in response.text.splitlines():
            if not line.strip():  # Skip empty lines
                continue
            record = json.loads(line.strip())
            yield {
                "_index": index_name,
                "_source": record
            }

    urls = [
        "https://sunmanapp.blob.core.windows.net/publicstuff/nintendo_games_embedded.json",
        "https://sunmanapp.blob.core.windows.net/publicstuff/ps_games_embedded.json",
        "https://sunmanapp.blob.core.windows.net/publicstuff/xbox_games_embedded.json"
    ]

    errors = []
    for url in urls:
        try:
            print(f"Indexing documents from {url}...")
            success, failed = helpers.bulk(es, generate_actions(url))
            print(f"Successfully indexed {success} documents.")
            print(f"Failed to index {failed} documents.")
        except helpers.BulkIndexError as e:
            errors.extend(e.errors)

    if not errors:
        return "Data has been successfully ingested into Elastic!"
    else:
        return "\n".join(errors)
