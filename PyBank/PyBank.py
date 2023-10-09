import csv
import os 
from pathlib import Path 

# Upload our Budget_Data CSV File
csvfile = "Resources/budget_data.csv"

# Output File
outputfile = "Analysis/budget_analysis.txt"

# Establish our Paramters
months = 0
previous_revenue = 0
month_of_change = []
list_revenue_change = []
highest_increase  = ["", 0]
highest_decrease  = ["", 9999999999999999999]
revenue = 0

# Read Into CSV Using CSV Reader
with open(csvfile) as PyBank_data:
    csvreader = csv.DictReader(PyBank_data)

    # Loop through the Dataset
    for row in csvreader:

        # Keep Track of Total Months and Revenue
        months = months + 1
        revenue = revenue + int(row["Profit/Losses"])

        # Calculate Revenue Change
        revenue_change = int(row["Profit/Losses"]) - previous_revenue
        previous_revenue = int(row["Profit/Losses"])
        list_revenue_change = list_revenue_change + [revenue_change]
        month_of_change = month_of_change + [row["Date"]]

        # Find the Highest Increase 
        if (revenue_change > highest_increase[1]):
            highest_increase[0] = row["Date"]
            highest_increase[1] = revenue_change

         # Find the Highest Decrease 
        if (revenue_change < highest_decrease[1]):
            highest_decrease[0] = row["Date"]
            highest_decrease[1] = revenue_change

#Calculate the Average Monthly Revenue Change
avg_revenue = sum(list_revenue_change) / len(list_revenue_change)

# Prepare Values for Output - "\n" is used to start a new line
output = (
    f"\nFinancial Analysis\n"
    f"-------------------------------\n"
    f"Total Months: {months}\n"
    f"Total Revenue: ${revenue}\n"
    f"Average Revenue Change: ${avg_revenue}\n"
    f"Greatest Increase in Revenue: {highest_increase[0]} (${highest_increase[1]})\n"
    f"Greatest Decrease in Revenue: {highest_decrease[0]} (${highest_decrease[1]})\n"
)

print(output)

# Export to Text File
with open(outputfile, "w") as txt_file:
    txt_file.write(output)

