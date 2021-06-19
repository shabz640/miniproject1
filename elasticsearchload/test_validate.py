import pytest
import big_to_smallcounter
import csv

csv_file = r'data.csv'

num_rows = 0
for row in open(csv_file):
    num_rows = num_rows + 1
chunk_size = 100
mod = num_rows % chunk_size
temp = []
idx = 0

with open(csv_file, "r") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        temp.append(row)
        idx = idx + 1
        if idx % chunk_size == 0:
            big_to_smallcounter.elastic_load(temp, idx)
            temp = []
        elif idx == num_rows - 1:
            big_to_smallcounter.elastic_load(temp, idx)
            temp = []
            index = idx

def test_validate():
    assert index == 288

