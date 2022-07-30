from pathlib import Path
import csv

file_path = Path.cwd()/"csv_report"/"Overheads.csv"

list = []

def Overheads():
    with file_path.open(mode = "r", encoding = "UTF-8") as data:
        reader = csv.reader(data)
        next(reader)

        
        

    


print(Overheads())