from audioop import reverse
from pathlib import Path
import csv
from re import T

file_path = Path.cwd()/"csv_report"/"Overheads.csv"

list = []

def overheads():
    with file_path.open(mode = "r", encoding = "UTF-8") as data:
        reader = csv.reader(data)
        next(reader)
        

        for lines in reader:
            print(lines)
            list.append(lines)
            sorted()
        
        

        return list
        # if list == reader("[Overheads]"):
        #     return reader
        
        
    
           


print(overheads())