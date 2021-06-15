#!/usr/bin/python3
import csv, json

csvFile = r'/home/sravindr/Downloads/data.csv'

class csvtojson():
    def __init__(self):
        pass

    def make_json(self, csvFile):
        with open(csvFile, "r") as f:
            reader = csv.reader(f)
            next(reader)
            data = []
            for row in reader:
                data.append(
                    {"Issue_Type": row[0], "Given_Name": row[1], "Expected_Name": row[2], "Result_Count": row[3],
                    "Is_Place_Name": row[4], "Expected_Distance": row[5]})

        return data
'''
conv = csvtojson()
res = conv.make_json(csvFile)
print(res)
'''