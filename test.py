from audioop import reverse
from pathlib import Path
import csv, re
from re import T

from pathlib import Path
import csv

file_path = Path.cwd()/"csv_report"/"Overheads.csv"

list = []
list2 = []

def Overheads():
    with file_path.open(mode = "r", encoding = "UTF-8") as data:
        reader = csv.reader(data)
        next(reader)
        
        for lines in reader:
            # print(lines)
            list2.append(lines)
            strlist2 = str(list2)
        print(strlist2)
            # print(strlist2)
        # for line in strlist2:
        #     print(line)
            # print(re.findall(pattern="Salary.+",string = line))



        # for file in reader:
        #     list.append(file[1])
        #     list.sort(key= float, reverse = True)

        # return list

print(Overheads())