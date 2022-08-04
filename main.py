import api, overheads, profit_loss,cash_on_hand, csv
from pathlib import Path

fp = Path.cwd()/"summary_report.csv"
fp.touch()
list3=[]
list4=[]
with fp.open(mode="w",encoding="UTF-8",newline="") as file:
    writer=csv.writer(file)
    writer.writerow([f"[REAL TIME CURRENCY CONVERSION RATE] USD1 = SGD{api.Exchange_rate}"])
    writer.writerow(overheads.Overheads())
    for rows in profit_loss.profitloss():
        writer.writerow([rows])
    for rows1 in cash_on_hand.cashonhand():
        writer.writerow([rows1])