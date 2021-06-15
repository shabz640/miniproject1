#!/usr/bin/python3
import json
import pandas as pd

csvFile = r'/home/sravindr/Downloads/data.csv'

class pandatojson():
    def __init__(self):
        pass

    def make_json(self, chunk):

        data = []
        for row in chunk.iterrows():
            print(row)
            print(chunk.to_json(orient='records', lines=True))
            data.append(
                {"Issue_Type": row[0], "Given_Name": row[1], "Expected_Name": row[2], "Result_Count": row[3],
                 "Is_Place_Name": row[4], "Expected_Distance": row[5]})


        return data




