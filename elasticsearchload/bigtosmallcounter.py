#!/usr/bin/python3
from elasticsearch import Elasticsearch, helpers
from csvtojson import csvtojson
import csv, json

csvFile = r'/home/sravindr/Downloads/data.csv'
num_rows = 0

for row in open(csvFile):
    num_rows += 1

#TEST -BRANCH
es = Elasticsearch()
conv = csvtojson()

json_data = conv.make_json(csvFile)
finalout = []
i = 0
j = 0
for value in json_data:
    i = i + 1
    j = j + 1
    finalout.append({'op_type': 'index', '_index': 'new-index1', '_type': '_doc', 'id': i, 'doc': value})
    if j == 100 or (num_rows - i) == 0:
        res = helpers.bulk(es, finalout)
        j = 0
        finalout = []

    else:
        pass
res1 = es.count(index='new-index1', doc_type='_doc', body={"query": {"match_all": {}}})["count"]
print(res1)

if res1 == num_rows + 1:
    print("Successful")
else:
    print("Failure")