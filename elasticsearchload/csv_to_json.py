#!/usr/bin/python3
import csv, json

class CsvToJson():
    def __init__(self):
        pass

    def make_json(self, csv_list):
        #with open(csv_file, mode= "r") as f:

        json_data = []
        for value in csv_list:
            print(value)
            json_data.append({"Issue_Type": value[0], "Given_Name": value[1], "Expected_Name": value[2],
                              "Result_Count": value[3], "Is_Place_Name": value[4], "Expected_Distance": value[5]})
        print (json_data)


'''
        with open(csv_file, "r") as f:
            reader = csv.reader(f)
            next(reader)
            data = []
            csv_chunk = []
            json_data = []
            j = 0
            for value in reader:
                csv_chunk.append(value)
                j = j + 1
                if (j % 100) or (j == 288):
                    for row in csv_chunk:
                        json_data.append({"Issue_Type": row[0], "Given_Name": row[1], "Expected_Name": row[2], "Result_Count": row[3], "Is_Place_Name": row[4], "Expected_Distance": row[5]})
                        csv_chunk = []
            return json_data
            '''



