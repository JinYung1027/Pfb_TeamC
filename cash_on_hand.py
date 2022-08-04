from pathlib import Path
import re, csv , api

csv_filepath = Path.cwd()/'csv_report'

def cashonhand():

    for csvdata in csv_filepath.glob('Cash on Hand.csv'):
            
        with csvdata.open(mode = 'r' , encoding= 'UTF-8') as file:

            x = 0

            data = file.read()

            datas = []

            cash = re.findall(pattern=r'[0-9][0-9][0-9]+' , string=data)

            cashsort = re.findall(pattern=r'[0-9][0-9][0-9]+' , string=data)

            cashsort.sort()

            startday = re.search(pattern=r'[0-9][0-9]' , string=data)

            startday = startday.group()

            if cash == cashsort:
                
                return('[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY')

            else:
                
                

                for x in range(0,5):

                    if float(cash[x+1]) < float(cash[x]) :
                        
                        deficit = float(cash[x]) - float(cash[x+1])

                        deficit = api.exc(deficit)

                        deficit = round(deficit , 2)

                        cd=([f'[CASH DEFICIT] DAY: {float(startday) + x + 1} , AMOUNT: SGD{deficit}'])

                        for c in cd:
                            datas.append(c)
                            
                return datas

                    

cashonhand()

                


    