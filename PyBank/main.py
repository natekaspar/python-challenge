import os

import csv

# Variables to store the data
total_months = 0
net_total = 0
greatest_increase = {"date": "", "amount": 0}
greatest_decrease = {"date": "", "amount": 0}
original_profit_loss = None
changes = []

# Connecting to csv file
csv_file_path = "/Users/natekaspar/Desktop/python-challenge/PyBank/Resources/budget_data.csv"

# Opening file
with open(csv_file_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skipping the first header row
    header = next(csvreader)

    # Looping through each row
    for row in csvreader:
        date, profit_loss = row

        # Making profit loss an integer
        profit_loss = int(profit_loss)

        # Getting the number of total months
        total_months = total_months + 1

        # Calculating Changes 
        if original_profit_loss is not None:
            change = profit_loss - original_profit_loss
            changes.append(change)

            # Greatest Increase and Decrease for profits
            if change > greatest_increase["amount"]:
                greatest_increase["date"] = date
                greatest_increase["amount"] = change
            elif change < greatest_decrease["amount"]:
                greatest_decrease["date"] = date
                greatest_decrease["amount"] = change

        # Storing the profit and loss for loop
        original_profit_loss = profit_loss

# Calculating net total 
net_total = sum(changes) + changes[0]

# Average change
if total_months > 1:
    average_change = sum(changes) / len(changes)
else: 
    average_change = 0

# Printing the results
print("Financial Analysis")
print("------------------")
print(f"Total Months: {total_months}")
print(f"Net Total Amount: ${net_total}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})")
print(f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})")
