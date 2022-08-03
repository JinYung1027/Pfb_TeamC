from pathlib import Path
import csv,re,api

#creating a variable to access overheads csv file. 
file_path = Path.cwd()/"csv_report"/"Overheads.csv"

#creating an empty set.
list = []
list2= []

#creating a function "overheads" to run the code.
def Overheads():

    #using file_path function to read the lines of csv file.
    with file_path.open(mode = "r", encoding = "UTF-8") as data:

        #creating a variable to read CSV File.
        reader = csv.reader(data)

        #function to skip the header in the CSV file.
        next(reader)

        #to assess the data in reader.
        for cost,data in reader:

            #creating a variable to access the api file.
            data=api.exc(float(data))

            #rearrange the overheads with catagory 
            a=f"{data},{cost.upper()}"

            #appending data into list
            list.append(a)

            #sorting list in a reverse order, from largest to smallest.
            list.sort(reverse=True)

            #The highest overhead in the game.
            highest_overhead=list[0]

            #Creating variable to find all percentages
            amount = re.findall(pattern="[0-9].+[0-9]",string=highest_overhead)

            #creating variable to find all expenses
            expense = re.findall(pattern="[A-Z].+[A-Z]",string=highest_overhead)

            #for function to access amount variable.
            for b in amount:

                #rounding float b to 2 decimal places. 
                b = round(float(b),2)

                #for function to access the expense variable.
                for c in expense:

                    #return the value for the function Overheads.
                    return[(f"[HIGHEST OVERHEADS] {c} : SGD{b}")]
            
Overheads()