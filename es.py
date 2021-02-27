from elasticsearch import Elasticsearch
from datetime import datetime

es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

el = {
    'updated_at': datetime.now()
}

for i in range(1, 4):
    es.indices.create(index='project_' + str(i))

for index in es.indices.get("project_*"):
    result = es.reindex({
        "source": {"index": index},
        "dest": {"index": "new_" + index}
    }, wait_for_completion=True, request_timeout=300)

    print(result)


for index in es.indices.get("new_project_*"):
    print(es.index(index=index, id=1, body=el))

for index in es.indices.get("new_project_*"):
    print(es.get(index=index, id=1)['_source'])
