# Elastic Game Guardian


https://github.com/sunileman/Elastic-Game-Guardian/assets/12245219/e8032edc-b136-419b-85ba-d68480cd646b


## UI
To launch the UI run
`streamlit run Elastic_Game_Guardian.py`


## Setup
Configure Azure OpenAI and Elasticsearch Cloud Service parameters in `variables.py`.  Add azure openAI key to `.streamlit/secrets.toml`


Example: `variables.py`

```
openai_api_type = "azure"
openai_api_base = "https://zzzzz.openai.azure.com"
openai_api_version = "2023-05-15"
es_username = 'elastic'
es_password = 'ess password'
es_cloudid = 'ess cloud id'
```

Example: `.streamlit/secrets.toml`

pass = "your azure openai key"