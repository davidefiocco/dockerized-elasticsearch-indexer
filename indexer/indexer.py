from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk

import time
time.sleep(30)   # follow Mihai Todor's suggestion on https://stackoverflow.com/questions/48711455/create-dockerized-elasticsearch-index-using-a-python-script-running-in-docker/48712414#48712414

es = Elasticsearch(hosts=[{"host":'elasticsearch'}])

data = [{'id': 1, 'foo': 'bar'}, {'id': 2, 'foo': 'spam'}]

actions = [
    {
    '_index' : 'test',
    '_type' : 'content',
    '_id' : str(item['id']),
    '_source' : item,
    }
for item in data
]

# create index
print("Indexing Elasticsearch db... (please hold on)")
bulk(es, actions)
print("...done indexing :-)")
