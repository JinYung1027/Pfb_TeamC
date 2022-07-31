from pathlib import Path
import re, csv

cwd = Path.cwd()/'project_group'
csv_filepath = Path.cwd()/'csv_report'/'Cash on Hand.csv'

def coh():    
    with csv_filepath.open(mode = 'r' , encoding= 'UTF-8') as file:

        reader=csv.reader(file)
        
        for text in reader:
            print(text)

coh()



    