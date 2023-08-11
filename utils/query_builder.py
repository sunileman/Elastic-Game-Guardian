import json
def build_query(embeddings, platform_selection):
    platform_mapping = {
        "Xbox": "XBOX",
        "PlayStation": "PS",
        "Nintendo": "NINTENDO"
    }

    query = {
        "knn": {
            "field": "openai_vector",
            "query_vector": embeddings,
            "k": 10,
            "num_candidates": 100
        },
        "fields": ["game_title", "platform"],
    }

    # If a specific platform is selected, add the filter term to the knn object.
    if platform_selection != "All":
        platform_value = platform_mapping.get(platform_selection, "")
        query["knn"]["filter"] = {
            "term": {
                "platform": platform_value
            }
        }

    print(json.dumps(query, indent=4))


    return query
