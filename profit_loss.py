from pathlib import Path
import csv, api


Path = Path.cwd()/"csv_report"/"Profit and Loss.csv"
list = []
listdiff = []
negative = []
days = []


def profitloss():

    with Path.open(mode = "r", encoding = "UTF-8", newline= "") as Path1:
        reader = csv.reader(Path1)
        next(reader)

        for lines in reader:
            floatlines = float(lines[4])
            list.append(floatlines)
            days.append(lines[0])
        
        count = 0
        for profit in list:
            difference = (list[count]-list[count-1])
            count += 1             
            
            if difference != list[0]-list[-1]:
                listdiff.append(difference)
        listdiff.insert(0,0)
        print(listdiff)
        
        for items in listdiff:
            if items<0:
                negative.append(items)
            
        if len(negative)==0:
            return("[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY]")
            
        elif len(negative)>0:
            for items in negative:
                index = (listdiff.index(items))
                Day=float(days[index])
                items = abs(items)
                items = round(api.exc(items),2)
                Profit_loss = (f"[PROFIT DEFICIT] DAY : {Day}, AMOUNT : SGD{items}")

                print(Profit_loss)
           


       



print(profitloss())