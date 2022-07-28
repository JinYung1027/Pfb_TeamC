from pathlib import Path
import csv

print(Path.cwd())
Path = Path.cwd()/"csv_report"/"Profit and Loss.csv"
print(Path.exists())
list = []

def profitloss():

    with Path.open(mode = "r", encoding = "UTF-8", newline= "") as Path1:
        reader = csv.reader(Path1)
        next(reader)

        for line in reader:
            list.append(line[4])
        if list[1]>line[2]:
            print("penis")

        
            


print(profitloss())