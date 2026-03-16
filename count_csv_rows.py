import csv

row_count = 0

with open("data.csv", "r") as file:
    csv_reader = csv.reader(file)
    
    for row in csv_reader:
        row_count += 1

print("Total number of rows in CSV file:", row_count)