from pathlib import Path
import csv,re,api

#creating a file path to access overheads csv file. 
file_path = Path.cwd()/"csv_report"/"Overheads.csv"

#create empty lists.
list = []
list2= []

#creating a function "overheads" to find the highest overhead expense
def Overheads():

    """
    - This function is to find the highest overhead expense in the game
    """

    #using file_path function to read the lines of csv file.
    with file_path.open(mode = "r", encoding = "UTF-8") as data:

        # Create a reader object using read() method
        reader = csv.reader(data)

        # next function to skip the header in the CSV file.
        next(reader)

        # Using for loop to assess the data in reader.
        for cost,data in reader:

            # Convert the data from USD to SGD by using the function created in api.py
            data=api.exc(float(data))

            #rearrange the data to a number first sequence for sorting later
            a=f"{data},{cost.upper()}"

            #append data into a list
            list.append(a)

            #sorting list in a reverse order, from largest to smallest.
            list.sort(reverse=True)

            #access to the highest overhead in the game by accessing to the first data.
            highest_overhead=list[0]

            # Create a variable to find the amount of the highest overhead expense
            amount = re.findall(pattern="[0-9].+[0-9]",string=highest_overhead)

            # Create a variable to find the expense of the highest overhead expense
            expense = re.findall(pattern="[A-Z].+[A-Z]",string=highest_overhead)

            #for loop to extract data needed from the two variable
            for b in amount:

                # convert b to float and round it into 2 d.p. 
                b = round(float(b),2)

                # for function to access the expense variable.
                for c in expense:

                    # return the value for the function Overheads.
                    return[(f"[HIGHEST OVERHEADS] {c} : SGD{b}")]
            
Overheads()