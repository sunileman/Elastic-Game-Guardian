from elasticsearch import helpers
from elasticsearch.helpers import BulkIndexError


def generate_bulk_data(records, index_name):
    for record in records:
        yield {
            "_index": index_name,
            "_source": record
        }


def bulk_index_to_es(es, records, index_name):
    actions = list(generate_bulk_data(records, index_name))

    try:
        success, failed = helpers.bulk(es, actions)
        failed_count = len(failed) if isinstance(failed, list) else 0
        return success, failed_count
    except BulkIndexError as e:
        print("Failed documents:", e.errors)
        return 0, len(actions)
