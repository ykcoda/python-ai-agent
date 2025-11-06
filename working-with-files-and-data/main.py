# READING CSV FILES IN PYTHON

import csv

with open("./model_logs.csv", "r") as csv_f:
    reader = csv.reader(csv_f)
    next(reader)

    token_data = {row[0]: int(row[3]) for row in reader}
    peak_day = max(token_data, key=token_data.get)

    print(peak_day)
