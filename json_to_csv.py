import json
import csv

# Sample JSON data (JSON array)
data = [
    {"Name": "Om", "Age": 19, "City": "Pune"},
    {"Name": "Rahul", "Age": 20, "City": "Mumbai"},
    {"Name": "Ankit", "Age": 21, "City": "Delhi"}
]

# Writing to CSV file
with open("output.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=data[0].keys())
    
    writer.writeheader()
    writer.writerows(data)

print("JSON data successfully converted to CSV.")