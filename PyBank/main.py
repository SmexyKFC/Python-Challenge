# The total number of months included in the dataset
# The net total amount of "Profit/Losses" over the entire period
# The changes in "Profit/Losses" over the entire period, and then the average of those changes
# The greatest increase in profits (date and amount) over the entire period
# The greatest decrease in profits (date and amount) over the entire period

import os
import csv

# Define PyBank's lists to store data
months = []
profit_loss_changes = []

# Defining PyBank Variables needed to calculate values
count_months = 0
net_profit_loss = 0
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

    # Header row 
    csv_header = next(csvfile)
             
    # Reading each row after the header
    for row in csv_reader:

        # count of months = count_months = count_months + 1
        count_months +=  1 

        # Assign current_month_profit_loss to value of each row
        # Add int to make sure numerical values are being inputed
        current_month_profit_loss = int(row[1])
        # Shows the values of row1 are properly assigned
        # print(current_month_profit_loss)
        
        # Finding the net profit
        # net_profit_loss = sum of all profit/loss 
        net_profit_loss += current_month_profit_loss
        # Shows the net profit after each calculation
        # print(net_profit_loss)

        if (count_months == 1):
            # Make the value of previous month to be equal to current month for the first data
            # This ensure the first data line is still used for analysis
            previous_month_profit_loss = current_month_profit_loss

        else:

            # Calculating profit/loss change 
                # Takes the next months profit/loss and subtracts by previous 
            profit_loss_change = current_month_profit_loss - previous_month_profit_loss
            # Print out the values after of each calculation to double check
            # print(profit_loss_change)

            # Add each month to the month list
            months.append(row[0])

            # Add each profit_loss_change calculations to the profit_loss_changes list
            profit_loss_changes.append(profit_loss_change)

            # Make the current_month_profit_loss to be the previous for the next calculation --> makes sure correct data points are being used 
            previous_month_profit_loss = current_month_profit_loss
        # End of loop

    # Finding total_profit_loss 
        # Add all values from the profit_loss_changes list
    total_profit_loss = sum(profit_loss_changes)
    # print(sum_profit_loss)

    # Finding the average profit/loss by taking total and dividing it by number of months --> minus 1 b/c we didnt use the first month
    # Formating to show 2 decimal points after calculating average
    average_profit_loss = round(total_profit_loss/(count_months-1), 2)
    # Used to check if average_profit_loss matched 
    # print(average_profit_loss)

    # Finding highest and lowest values in profit/loss changes list 
    # Use max/min function on profit_loss_changes list
    highest_change = max(profit_loss_changes)
    lowest_change = min(profit_loss_changes)

    # Index value of highest and lowest changes in profit/losses 
    # Using the lowest/highest values to find corresponding index in profit/loss changes list
    highest_month_index = profit_loss_changes.index(highest_change)
    # print(highest_month_index)
    lowest_month_index = profit_loss_changes.index(lowest_change)
    # print(lowest_month_index)

    # Finding best and worst month 
    # Using the index to find the corresponding months
    best_month = months[highest_month_index]
    # print(best_month)
    worst_month = months[lowest_month_index]
    # print(worst_month)

# Analysis Report
# Using old method to print strings
print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(count_months))
print("Total: $"  +str(net_profit_loss))
print("Average Change: $" + str(average_profit_loss))
print("Greatest Increase in Profits: " +str(best_month) + "($" + str(highest_change) + ")")
print("Greatest Decrease in Losses: " +str(worst_month) + "($" + str(lowest_change) + ")")



# Exporting text file
Analysis_file = os.path.join("Analysis", "Analysis_data.txt")
with open(Analysis_file, "w") as outfile:
    # Using /n to make a new line in text file 
    # Using f method to print string
    outfile.write("Financial Analysis\n")
    outfile.write("----------------------------\n")
    outfile.write(f"Total Months:  {count_months}\n")
    outfile.write(f"Total:  ${net_profit_loss}\n")
    outfile.write(f"Average Change:  ${average_profit_loss}\n")
    outfile.write(f"Greatest Increase in Profits:  {best_month} (${highest_change})\n")
    outfile.write(f"Greatest Decrease in Losses:  {worst_month} (${lowest_change})\n")