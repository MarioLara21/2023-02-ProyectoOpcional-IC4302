import os
from elasticsearch import Elasticsearch

# Read environment variables
elasticsearch_host = os.environ.get("ELASTICSEARCH_HOST")
index_name = os.environ.get("INDEX_NAME", "jobs")

# Connect to Elasticsearch
es = Elasticsearch([elasticsearch_host])

# Create an index
es.indices.create(index=index_name)

print(f"Index '{index_name}' created in Elasticsearch.")