# Import the required libraries
from elasticsearch import Elasticsearch, helpers
import json

from utils.es_config import index_name, settings, mappings, embedded_file_name, deleteExistingIndex
from utils.es_helper import create_es_client, manage_index
from variables import es_username, es_cloudid, es_password

try:

    username = es_username
    password = es_password
    cloudid = es_cloudid

    # get es object
    es = create_es_client(username, password, cloudid)

    print(es.info())
except Exception as e:
    print("Connection failed", e.errors)

##create index
manage_index(es, index_name, settings, mappings, deleteExistingIndex)


def generate_actions(filename):
    with open(filename, 'r') as f:
        for line in f:
            record = json.loads(line.strip())
            yield {
                "_index": index_name,
                "_source": record
            }


# Ingest data using the helpers.bulk method
try:
    print(f"Indexing documents...")
    success, failed = helpers.bulk(es, generate_actions(embedded_file_name))
    print(f"Successfully indexed {success} documents.")
    print(f"Failed to index {failed} documents.")
except helpers.BulkIndexError as e:
    print(e)
    for error_detail in e.errors:
        print(error_detail)
