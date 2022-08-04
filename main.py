# Import module and functions needed for writing the csv file
import api, overheads, profit_loss,cash_on_hand, csv
from pathlib import Path

# Create a file path to the new file named "summary_report.csv" in the current working directory.
fp = Path.cwd()/"summary_report.txt"

# Create the file "summary_report.csv" in current working directory using .touch() method
fp.touch()

# Open the csv file in write mode by using the .open() method
with fp.open(mode="w",encoding="UTF-8",newline="") as file:

    # Create a write object and name it as "writer" using csv.writer() from csv module
    writer=csv.writer(file)
    # Use .writerow() to write all the datas into the csv file
    writer.writerow([f"[REAL TIME CURRENCY CONVERSION RATE] USD1 = SGD{api.Exchange_rate}"])
    writer.writerow(overheads.Overheads())
    # Use for loop to write the data that might have one or more outcome
    for rows in profit_loss.profitloss():
        writer.writerow([rows])
    for rows1 in cash_on_hand.cashonhand():
        writer.writerow([rows1])