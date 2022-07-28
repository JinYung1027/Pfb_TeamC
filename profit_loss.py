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

        for lines in reader:
            print(lines[4])
            list.append(lines[4])          
        
        for items in list:
            difference = items - items
             


print(profitloss())