# Import module and functions needed for writing the csv file
import api, overheads, profit_loss,cash_on_hand, csv
from pathlib import Path


def main():

# Create a file path to the new file named "summary_report.csv" in the current working directory.
    fp = Path.cwd()/"summary_report.txt"

# Create the file "summary_report.csv" in current working directory using .touch() method
    fp.touch()

# Open the csv file in write mode by using the .open() method
    with fp.open(mode="w") as file:
        
        file.write(f"[REAL TIME CURRENCY CONVERSION RATE] USD1 = SGD{api.Exchange_rate}" + "\n")
        file.write(overheads.Overheads() + "\n")
    # Use for loop to write the data that might have one or more outcome
        for rows1 in cash_on_hand.cashonhand():
            file.write(rows1 + "\n")
        for rows in profit_loss.profitloss():
            file.write(rows + "\n")


main()