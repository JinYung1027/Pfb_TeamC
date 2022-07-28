from pathlib import Path
import csv
from re import T

file_path = Path.cwd()/"csv_report"/"Overheads.csv"

list = []

def overheads():
    with file_path.open(mode = "r", encoding = "UTF-8") as data:
        reader = csv.reader(data)
        next(reader)

        for file in reader:
            list.append(file[1])
            list.sort(key = float, reverse= True)
        print(list)
        # if list == reader("[Overheads]"):
        #     return reader

print(overheads())
        



