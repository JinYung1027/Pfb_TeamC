from pathlib import Path
import re, csv , api

# Creating file path to 'csv_reports'
csv_filepath = Path.cwd()/'csv_report'

# Creating a function to check for cash surplus or deficit
def cashonhand():
    """
    This function checks if cash on hand is consecutively increase everyday,
    also known as a surplus.
    If cash on hand isn't consecutively increasing, this function will find out
    which day did the cash deficit happened,
    and how much was the deficit
    """
    
    # Using .glob() to return the Cash on Hand.csv file
    for csvdata in csv_filepath.glob('Cash on Hand.csv'):
        
        # Using .open() to encode the csv file
        with csvdata.open(mode = 'r' , encoding= 'UTF-8') as file:
            
            # Using .read() to read the file that has been encoded previously
            data = file.read()

            # Creating an empty set
            datas = []

            # Using RegEx .findall() function to find the values for cash on hand
            cash = re.findall(pattern=r'[0-9][0-9][0-9].+' , string=data)

            # List comprehension to convert the data into float
            cash = [float(n) for n in cash]
            
            # Using RegEx .findall() function to find the values for cash on hand again (for an actual purpose)
            cashsort = re.findall(pattern=r'[0-9][0-9][0-9].+' , string=data)

            # List comprehension to convert the data into float
            cashsort = [float(p) for p in cashsort]

            # Sorting the numbers in cashsort in ascending numbers
            cashsort.sort()

            # Using RegEx .search() function to find which day is the first day that data is extracted
            startday = re.search(pattern=r'[0-9][0-9]' , string=data)

            # Using .group() to get the number
            startday = startday.group()
            
            # Using if statement to determine if there is a cash surplus or not
            if cash == cashsort:
                
            """
            IF CASH ON HAND IS CONSECUTIVELY INCREASING EVERYDAY,
            SORTING cash IN ASCENDING ORDER WOULD GET YOU THE SAME SEQUENCE AS cash.
            THEREFORE cash == cashsort IF THERE IS A SURPLUS
            """
                # Printing the statement for cash surplus if there is a cash surplus
                return(['[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY'])

            else:
                
                
                # for loop to determine which day has a deficit
                for x in range(0,(len(cash)-1)):

                    # if statement to determine if cash on hand on 'x' day is lower than previous day
                    if float(cash[x+1]) < float(cash[x]) :
                        
                        # Calculating the deficit
                        deficit = float(cash[x]) - float(cash[x+1])

                        # Converting deficit from USD to SGD
                        deficit = api.exc(deficit)

                        # Rounding off deficit to 2 decimal places
                        deficit = round(deficit , 2)

                        # Creating a variable to store the statement that is to be printed out when there is a deficit
                        # Statement consist of the day and the deficit value in SGD
                        cd=([f'[CASH DEFICIT] DAY: {float(startday) + x + 1} , AMOUNT: SGD{deficit}'])

                        # Using .append() to store all statements before printing
                        for c in cd:
                            datas.append(c)
                # Returning all statements            
                return datas

                    

cashonhand()

                


    
