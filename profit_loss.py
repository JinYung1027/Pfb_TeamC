from pathlib import Path
import csv, api

# Create file path and extend to "csv_report" and "Profit and Loss.csv"
Path = Path.cwd()/"csv_report"/"Profit and Loss.csv"

## Create lists for the coding in the function
# Create list 'list' to contain Net profit from csv file
list = []
# Create list 'listdiff' to contain differences of net profit between each day
listdiff = []
# Create list 'negative' to contain negative differences of net profit if any
negative = []
# Create list 'days' to contain Days from csv file
days = []
# Create list 'PL' to store the all possible outcome
PL=[]

# Define function
def profitloss():
    """
    - This function extracts the net profit of each day and calculate the differences
    - It will determine whether the net profit is consecutively higher each day
    """

    # return value of file open is assigned to variable 'path1' after as keyword
    with Path.open(mode = "r", encoding = "UTF-8", newline= "") as Path1:
        # instantiate a reader object and assign it to variable 'reader'
        reader = csv.reader(Path1)
        # use 'next()' to skip the header.
        next(reader)

        # Create for loop to iterate through csv file
        for lines in reader:
            # convert extracted net profit values from string to float to allow it to be computable
            floatlines = float(lines[4])
            # append float values into list 'list'
            list.append(floatlines)
            # append Days into list 'days' by indexing 
            days.append(lines[0])
        
        # create variable 'count' to act as counter
        count = 0
        # Create for loop to iterate through list 'list'
        for profit in list:
            # Calculate the difference in net profit between days
            difference = (list[count]-list[count-1])
            # This allows the counter 'count' to increase by one for each loop
            # With an increase in the counter 'count', it allows the difference to be calculated continously for all the days extracted
            count += 1             
            
            # Exclude the first value calculated as it is not needed using if statement
            if difference != list[0]-list[-1]:
                # append the differences calculated into list 'listdiff'
                listdiff.append(difference)
        # insert '0' infront of the list 'listdiff' to allow the indexing to work later on
        listdiff.insert(0,0)
       
        # Create loop to iterate through listdiff
        for items in listdiff:
            # If the differences in net profit is negative, append it into the list 'negative'
            if items<0:
                negative.append(items)
                
        # If there are no items in the list 'negative', it means that the net profit is consecutively higher
        if len(negative)==0:
            # Create a variable to store "[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY]"
            Profit_surplus=["[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY"]
            # Return the message from Profit_surplus
            return(Profit_surplus)
            
        # If there are items in the list 'negative', execute the following code
        elif len(negative)>0:
            # Create a loop to iterate through list 'negative'
            for items in negative:
                # Find the index of the negative difference in the list 'listdiff'
                index = (listdiff.index(items))
                # Find the day where there is a profit deficit using the index found
                Day=float(days[index])
                # Convert the negative values into positive values 
                items = abs(items)
                # Use function created in imported module to convert the values from USD into SGD
                items = round(api.exc(items),2)
                # Assign the final statement into the variable 'Profit_loss'
                Profit_deficit = ([f"[PROFIT DEFICIT] DAY : {Day}, AMOUNT : SGD{items}"])
                # for loop to append all possible outcome in this 'PL' list
                for i in Profit_deficit:
                    PL.append(i)

                    
                    
            # return the list
            return(PL)
                
           