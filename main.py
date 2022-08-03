import api, profit_loss, csv
from pathlib import Path

fp = Path.cwd()/"summary_report.csv"
fp.touch()

with fp.open(mode="w",encoding="UTF-8",newline="") as file:
    writer=csv.writer(file)
    writer.writerow([f"[REAL TIME CURRENCY CONVERSION RATE] USD1 = SGD{api.Exchange_rate}"])
    writer.writerows([profit_loss.profitloss()])