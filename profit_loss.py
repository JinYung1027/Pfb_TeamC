from pathlib import Path
import csv

# print(Path.cwd())
Path = Path.cwd()/"csv_report"/"Profit and Loss.csv"
# print(Path.exists())
list = []
listdiff = []
negative = []
positive = []
# print(len(list))

def profitloss():

    with Path.open(mode = "r", encoding = "UTF-8", newline= "") as Path1:
        reader = csv.reader(Path1)
        next(reader)

        for lines in reader:
            floatlines = float(lines[4])
            list.append(floatlines)
        print(list)
        
        count = 0
        for profit in list:
            difference = (list[count]-list[count-1])
            count += 1             
            
            if difference != list[0]-list[-1]:
                listdiff.append(difference)
        print(listdiff)
        
        for items in listdiff:
            if items<0:
                negative.append(items)
            else:
                positive.append(items)

        if len(negative)==0:
            return("[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY]")
            
        elif len(negative)>0:
            return("Profit Deficit")


        
            
                

                
                
                
                   
                    
                #    return("[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY]")
                
        



        


       



print(profitloss())