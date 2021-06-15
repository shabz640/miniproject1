#!/usr/bin/python3
import pandas as pd
import sys
import json, csv
from pprint import pprint
from csvtojson import csvtojson
from pandatojson import pandatojson
from elasticsearch import Elasticsearch, helpers

csvFile = r'/home/sravindr/Downloads/data.csv'
num_rows = -1

for row in open(csvFile):
    num_rows += 1

#print(num_rows)



es = Elasticsearch()
conv = pandatojson()

chunk_size = 100
batch_no = 1

i = 1

for chunk in pd.read_csv(csvFile, chunksize=chunk_size):
    finalout = []
    jsonFile =  json.loads(chunk.to_json(orient='records'))


    for value in jsonFile:
        print(value)
        finalout.append({'op_type': 'index', '_index': 'new-index1', '_type': '_doc', 'id': i, 'doc': value})
        i = i + 1
    res = helpers.bulk(es, finalout)
res1 = es.count(index='new-index1', doc_type='_doc', body={"query": {"match_all":{}}})["count"]

print(res1)

if res1 == num_rows:
    print("Successful")
else:
    print("Failure")

