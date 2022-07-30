from pathlib import Path
import csv

# print(Path.cwd())
Path = Path.cwd()/"csv_report"/"Profit and Loss.csv"
# print(Path.exists())
list = []
lanjiao = []

def profitloss():

    with Path.open(mode = "r", encoding = "UTF-8", newline= "") as Path1:
        reader = csv.reader(Path1)
        next(reader)

        for lines in reader:
            penis = float(lines[4])
            list.append(penis)
        print(list)
        
        count = 0
        for profit in list:
            balls = (list[count]-list[count-1])
            count += 1             
            
            if balls != list[0]-list[-1]:
                lanjiao.append(balls)
        print(lanjiao)

        for items in lanjiao:
            if items>0:
                Profit = "Surplus"
            else:
                Profit = "Deficit"
                
                if Profit == "Deficit":
                    print("penis")

                else:
                    print("penis2")

                
                
                
                   
                    
                #    return("[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY]")
                
        



        # count = 0
        # for profit in list:
        #     print(list[count])
            


        #   list = float(list)
        #   difference = list[count]-list[count-1]
        #   print(difference)
        # print(list[count])
          



print(profitloss())