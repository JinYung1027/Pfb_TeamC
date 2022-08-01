from pathlib import Path
import csv,re,api

file_path = Path.cwd()/"csv_report"/"Overheads.csv"

list = []
list2= []
def Overheads():
    with file_path.open(mode = "r", encoding = "UTF-8") as data:
        reader = csv.reader(data)
        next(reader)
        for cost,data in reader:
            data=api.exc(float(data))
            a=f"{data},{cost.upper()}"
            list.append(a)
            list.sort(reverse=True)
            highest_overhead=list[0]
            amount = re.findall(pattern="[0-9].+[0-9]",string=highest_overhead)
            expense = re.findall(pattern="[A-Z].+[A-Z]",string=highest_overhead)
            for b in amount:
                b = round(float(b),2)
                for c in expense:
                    return(f"[HIGHEST OVERHEADS] {c} : SGD{b}")
            

print(Overheads())