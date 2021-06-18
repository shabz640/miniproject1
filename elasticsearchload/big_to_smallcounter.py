#!/usr/bin/python3
from elasticsearch import Elasticsearch, helpers
from csv_to_json import CsvToJson
import csv

es = Elasticsearch()
conv = CsvToJson()

csv_file = r'data.csv'

num_rows = 0
for row in open(csv_file):
    num_rows = num_rows + 1
chunk_size = 100
mod = num_rows % chunk_size

temp = []

index = 0


def elastic_load(data, index):
    final_out = []
    json_data = []
    if index == num_rows - 1:
        index = index - mod + 1
    else:
        index = index - chunk_size
    for value in data:
        json_data.append({"Issue_Type": value[0], "Given_Name": value[1], "Expected_Name": value[2],
                          "Result_Count": value[3], "Is_Place_Name": value[4], "Expected_Distance": value[5]})

    for chunk in json_data:
        index = index + 1
        final_out.append({'op_type': 'create', '_index': 'new-index1', '_type': '_doc', 'id': index, 'doc': chunk})

    res = helpers.bulk(es, final_out)
    print(index)




idx = 0
with open(csv_file, "r") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        temp.append(row)
        idx = idx + 1
        if idx % chunk_size == 0:
            elastic_load(temp, idx)
            temp = []
        elif idx == num_rows - 1:
            elastic_load(temp, idx)
            temp = []
            index = idx

print(index)

'''
def validate(id):
    res = es.search(index='new-index1', body={"query": {"match": {"id": id}}})
    for hit in res['hits']['hits']:
        return hit["_source"]["doc"]["Expected_Name"]

'''