from pathlib import Path
import csv, api

print(Path.cwd())
Path = Path.cwd()/"csv_report"/"Profit and Loss.csv"
# print(Path.exists())
list = []
listdiff = []
negative = []

days = []
# print(len(list))

def profitloss():

    with Path.open(mode = "r", encoding = "UTF-8", newline= "") as Path1:
        reader = csv.reader(Path1)
        next(reader)

        for lines in reader:
            floatlines = float(lines[4])
            list.append(floatlines)
            days.append(lines[0])
        print(days)
        print(list)
            # print(lines[0])
        #     days.append(lines1)
        # print(days)
        
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
            # else:
            #     positive.append(items)

        if len(negative)==0:
            return("[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY]")
            
        elif len(negative)>0:
            # print(listdiff.index(-128834.0))
            for items in negative:
                index = (listdiff.index(items))
                Amount=(list[index])
                Day=float(days[index])
                items = abs(items)
                items = round(api.exc(items),2)
                print(items)
            return f"[PROFIT DEFICIT] DAY : {Day}, AMOUNT : SGD{items}"
           


       



print(profitloss())