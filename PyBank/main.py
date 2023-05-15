
# Modules 
import os
import csv

# Define PyBank's lists to store data
months = []
profit_loss_changes = []

# Defining PyBank Variables needed to calculate values
count_months = 0
net = 0
previous_month_profit_loss = 0
current_month_profit_loss = 0
profit_loss_change = 0


# Change directory to the directory with Python script 
# Allows us to get the directory path of any given file
os.chdir(os.path.dirname(__file__))

# Creating a path to to resources folder to collect data
budget_data_csv = os.path.join("Resources", "budget_data.csv")


# Open and read csv
with open(budget_data_csv,'r') as csvfile:
    # Determining delimiter 
    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

    for row in csv_reader:

        # count of months = count_months + 1
        count_months +=  1 

        # Assign current_month_profit_loss to value of each row
        current_month_profit_loss = int(row[1])

        # net = sum of all monthly profit/loss 
        net += current_month_profit_loss

        if (count_months == 1):
            # This ensure the first data line is still used for analysis
            previous_month_profit_loss = current_month_profit_loss

        else:
            # Calculating profit/loss change 
            # Takes the next months profit/loss and subtracts by previous 
            profit_loss_change = current_month_profit_loss - previous_month_profit_loss

            # Add each month to the month list
            months.append(row[0])

            # Add each profit_loss_change calculations to the profit_loss_changes list
            profit_loss_changes.append(profit_loss_change)

            # Make the next previous_profit_loss value to be the previous current_profit_loss value for next calculation 
            previous_month_profit_loss = current_month_profit_loss 
        # End of loop

    # Finding total_profit_loss 
    total_profit_loss_changes = sum(profit_loss_changes)

    # Finding the average profit/loss --> minus 1 b/c we didnt use the first month
    # Formating to show 2 decimal points 
    average_profit_loss = round(total_profit_loss_changes/(count_months-1), 2)
   
    # Finding highest and lowest values in profit/loss changes list 
    highest_change = max(profit_loss_changes)
    lowest_change = min(profit_loss_changes)

    # Using the lowest/highest values to find corresponding index in profit/loss changes list
    highest_month_index = profit_loss_changes.index(highest_change)
    lowest_month_index = profit_loss_changes.index(lowest_change)
 
    # Using the index to find the corresponding months
    best_month = months[highest_month_index]
    worst_month = months[lowest_month_index]


# Analysis Report --> Terminal
print(f"Financial Analysis")
print(f"----------------------------")
print(f"Total Months: {count_months}")
print(f"Total: ${net}")
print(f"Average Change: ${average_profit_loss}")
print(f"Greatest Increase in Profits: {best_month}  (${highest_change})")
print(f"Greatest Decrease in Losses: {worst_month}  (${lowest_change})")

# Exporting text file
Analysis_file = os.path.join("Analysis", "Analysis_data.txt")
with open(Analysis_file, "w") as outfile:
    # Using /n to make a new line in text file 
    outfile.write("Financial Analysis\n")
    outfile.write("----------------------------\n")
    outfile.write(f"Total Months:  {count_months}\n")
    outfile.write(f"Total:  ${net}\n")
    outfile.write(f"Average Change:  ${average_profit_loss}\n")
    outfile.write(f"Greatest Increase in Profits:  {best_month}  (${highest_change})\n")
    outfile.write(f"Greatest Decrease in Losses:  {worst_month}  (${lowest_change})\n")