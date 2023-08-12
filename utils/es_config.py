index_name = 'games'
number_of_dims = 1536
similarity = "dot_product"
rate_throttle = .2
deleteExistingIndex = True

########for xbox file processing#######
'''
embedded_file_name="./output/xbox_games_embedded.json"
source_file_type = "xbox"
source_file_name = "./files/xbox_one_games.csv"
'''

##for playstation file processing#######
'''
embedded_file_name = "./output/ps_games_embedded.json"
source_file_type = "ps"
source_file_name = "./files/ps4.csv"
'''

##for nintendo file processing#######

embedded_file_name = "./output/nintendo_games_embedded.json"
source_file_type = "nintendo"
source_file_name = "./files/nintendo.csv"

settings = {
    "number_of_shards": 2,
    "number_of_replicas": 1
}

# Mapping Specification
mappings = {
    "properties": {
        "name": {
            "type": "keyword",
        },
        "platform": {
            "type": "keyword"
        },
        "openai_vector": {
            "type": "dense_vector",
            "index": "true",
            "similarity": similarity,
            "dims": number_of_dims
        }
    }
}
