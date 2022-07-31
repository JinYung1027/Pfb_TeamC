from pathlib import Path
import csv

file_path = Path.cwd()/"csv_report"/"Overheads.csv"

list = []
list2= []
def Overheads():
    with file_path.open(mode = "r", encoding = "UTF-8") as data:
        reader = csv.reader(data)
        next(reader)
        for cost,data in reader:
            data=float(data)
            a=f"{data},{cost}"
            list.append(a)
            list.sort(reverse=True)
            highest_overhead=list[0]
            return(highest_overhead)