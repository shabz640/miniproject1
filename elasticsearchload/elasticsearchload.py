#!/usr/bin/python3
import sys
import json
from pprint import pprint
from csvtojson import csvtojson
from elasticsearch import Elasticsearch, helpers

es = Elasticsearch(timeout=30)
newjson = csvtojson()

csvFile = r'/home/sravindr/Downloads/data.csv'
#jsonFile = r'/home/sravindr/Downloads/data.json'


class ElasticLoad():
    def __init__(self):
        pass
        #TODO

    def elasticload(self):
        json_data = newjson.make_json(csvFile)
        i = 1
        finalout = []
        for value in json_data:
            finalout.append({'op_type': 'index','_index': 'new-index','_type':'_doc', 'id': i, 'doc': value })
            i = i + 1
        return finalout

e = ElasticLoad()
e_obj = e.elasticload()
res=helpers.bulk(es,e_obj)

'''
    def insert_data(self):
        i = 1
        finalout = []
        for value in json_data:
'''



