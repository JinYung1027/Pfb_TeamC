import api, overheads, profit_loss,cash_on_hand, csv
from pathlib import Path

fp = Path.cwd()/"summary_report.csv"
fp.touch()

with fp.open(mode="w",encoding="UTF-8",newline="") as file:
    writer=csv.writer(file)
    writer.writerow([f"[REAL TIME CURRENCY CONVERSION RATE] USD1 = SGD{api.Exchange_rate}"])
    writer.writerow(overheads.Overheads())
    writer.writerows([profit_loss.profitloss()])
    writer.writerows([cash_on_hand.cashonhand()])
