import csv

with open('example_csv_format') as f:
    reader = csv.reader(f)
    for row in reader:
        if row:
            print(row)

