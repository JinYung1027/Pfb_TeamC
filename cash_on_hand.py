from pathlib import Path
import re, csv

cwd = Path.cwd()/'project_group'
csv_filepath = Path.cwd()/'csv.reports'
for csvdata in csv_filepath.glob('Cash on Hand.csv'):
    
    with csvdata.open(mode = 'r' , encoding= 'UTF-8') as file:

        data = file.read()

        print(data)



    