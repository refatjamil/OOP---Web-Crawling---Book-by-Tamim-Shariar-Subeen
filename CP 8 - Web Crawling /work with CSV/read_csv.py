import csv

with open('book.csv', newline='') as csvfile:
    csv_reader  = csv.reader(csvfile)
    for row in csv_reader:
        print(row)