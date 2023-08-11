# Import the required libraries
import openai
import eland as ed
import pandas as pd
from utils.es_config import settings, mappings, index_name, source_file_name, source_file_type, \
    embedded_file_name
from utils.es_helper import create_es_client, manage_index
from utils.data_utils import prepare_data
import streamlit as st

import json

from utils.bulk_utils import bulk_index_to_es
from variables import es_username, es_password, es_cloudid, openai_api_type, openai_api_version, openai_api_base

openai.api_type = openai_api_type
openai.api_base = openai_api_base
openai.api_version = openai_api_version
openai.api_key = st.secrets['pass']

print("pandas version:", pd.__version__)
print("eland version:", ed.__version__)

try:

    username = es_username
    password = es_password
    cloudid = es_cloudid

    # get es object
    es = create_es_client(username, password, cloudid)

    print(es.info())
except Exception as e:
    print("Connection failed", e.errors)

file_path = source_file_name
records = prepare_data(file_path, source_file_type)

with open(embedded_file_name, 'w') as f:
    for record in records:
        f.write(json.dumps(record))
        f.write('\n')
