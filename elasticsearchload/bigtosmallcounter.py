#!/usr/bin/python3
from elasticsearch import Elasticsearch, helpers
from csvtojson import csvtojson
import csv, json

es = Elasticsearch()
conv = csvtojson()

csvFile = r'data.csv'
num_rows = 0

for row in open(csvFile):
    num_rows += 1
print(num_rows)


json_data = conv.make_json(csvFile)

finalout = []
i = 0
for value in json_data:
    i = i + 1
    finalout.append({'op_type': 'index', '_index': 'new-index1', '_type': '_doc', 'id': i, 'doc': value})
    if (i % 100 == 0) or (i == num_rows - 1):
        res = helpers.bulk(es, finalout)
        finalout = []

    else:
        pass
print(i)

if i == num_rows -1 :
    print("Successful")
else:
    print("Failure")
