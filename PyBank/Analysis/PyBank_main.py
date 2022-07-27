import os
import csv

#file_to_load = os.path.join("budget_data.csv")
file_to_load = os.path.join("Resources", "budget_data.csv")
# print (file_to_load)

total_profit_losses = 0
current = 0
last = 0

total_change = 0
months = 0

# The greatest increase in profits (date and amount) over the entire period
greatest_increase = 0
greatest_increase_name = ""

# The greatest decrease in profits (date and amount) over the entire period
greatest_decrease = 99999999
greatest_decrease_name = ""

# initializing the titles and rows list
csv_headers = []
rows = []

with open(file_to_load, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)
    # print(csvreader)

    # extracting field names through first row
    csv_headers = next(csvreader)
    # print(csv_headers)

    # extracting each data row one by one
    for row in csvreader:
        # print(row)
        rows.append(row)

    # print(rows)

# The total number of months included in the dataset
Total_Months = len(rows)

# The net total amount of "Profit/Losses" over the entire period
total_profit_losses = len()
