import statistics
import csv
import os

# declare & initialize variables
profit_list = []
months_list = []
profit_change_list = []


#open csv file
csvpath = os.path.join('Resources','budget_data.csv')
with open(csvpath,'r') as csvfile:
    #split the data on commas
    csvreader = csv.reader(csvfile,delimiter = ',')
    # skip first line
    csv_header = next(csvreader)

    # read in csv rows into two lists: months and profits
    for rows in csvreader:
        months_list.append(rows[0])
        profit_list.append(int(rows[1]))
        
        
        
# calculate list of monthly profit changes        
for i in range(1,len(profit_list)):
    profit_change_list.append(profit_list[i] - profit_list[i-1])


# Begin report calculations
with open("analysis/pybank.txt","w") as txt_file:
        
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {len(months_list)}")
    print(f"Total: ${sum(profit_list):,}")

    txt_file.write("Financial Analysis\n")
    txt_file.write("----------------------------\n")
    txt_file.write(f"Total Months: {len(months_list)}\n")
    txt_file.write(f"Total: ${sum(profit_list):,}\n")


    # Calculate and print average change
    print(f"Average Change: ${round(    statistics.mean(profit_change_list),2    ):,}")
    txt_file.write(f"Average Change: ${    round(statistics.mean(profit_change_list),2    ):,}\n")

    # find max profit change, return index location of said value
    index = profit_change_list.index(    max(profit_change_list)    )
    print(f"Greatest Increase in Profits: {months_list[index + 1]} $({profit_change_list[index]:,})")
    txt_file.write(f"Greatest Increase in Profits: {months_list[index + 1]} $({profit_change_list[index]:,})\n")

    # find minimum, same idea
    index = profit_change_list.index(    min(profit_change_list)    )
    print(f"Greatest Decrease in Profits: {months_list[index + 1]} $({profit_change_list[index]:,})")
    txt_file.write(f"Greatest Decrease in Profits: {months_list[index + 1]} $({profit_change_list[index]:,})\n")