# Import module and functions needed for writing the text file
import api, overheads, profit_loss,cash_on_hand, csv
from pathlib import Path

# Create a function to write the data into text file
def main():

# Create a file path to the new file named "summary_report.txt" in the current working directory.
    fp = Path.cwd()/"summary_report.txt"

# Create the file "summary_report.txt" in current working directory using .touch() method
    fp.touch()

# Open the csv file in write mode by using the .open() method
    with fp.open(mode="w") as file:

        # .write() method writes data to a plain text file
        ## added a "\n" to create a new line before the next data
        file.write(f"[REAL TIME CURRENCY CONVERSION RATE] USD1 = SGD{api.Exchange_rate}" + "\n")
        file.write(overheads.Overheads() + "\n")
    # Use for loop to write the data that might have one or more outcome
        for rows1 in cash_on_hand.cashonhand():
            file.write(f"{rows1}" + "\n")
        for rows in profit_loss.profitloss():
            file.write(f"{rows}" + "\n")

# Execute the function
main()