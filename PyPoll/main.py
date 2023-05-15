
# Modules
import os
import csv

# Change directory to the directory with Python script 
# Allows us to get the directory path of any given file
os.chdir(os.path.dirname(__file__))

# Creating a path to to resources folder to collect data
election_data_csv = os.path.join("Resources", "election_data.csv")

# Setting up variables and dictionary
total_votes = 0 

votes_per_candidate = {}

with open(election_data_csv, newline='') as csvfile:

    # Determining delimiter 
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    # Read each row of data after the header
    for row in csvreader:
        # total votes = total votes + 1 
        total_votes += 1
        # Assigning candidate from csv to a variable
        name = row[2]
        if name in votes_per_candidate:
            # Adds vote count if the candidate name is in dictionary
            votes_per_candidate[name] += 1
        else:
            # Gives value of 1 to candidate name if name is not in dictionary
            votes_per_candidate[name] = 1   
            
        
    
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")

# Code to print out candidate name + vote percentage + total votes per candidate
# Using .items() to return dictionary key-value pairs
for candidate, votes in votes_per_candidate.items():
    # Using percentage string format to show 3 decimal places
    print(candidate + ": " + "{:.3%}".format(votes/total_votes) + "   (" +  str(votes) + ")")
    
print("-------------------------") 
# Finding the max value in voter_per_candidate list
# Getting the voter_per_candidate key will give us the candidate name for winnder
winner = max(votes_per_candidate, key=votes_per_candidate.get)

print(f"Winner: {winner}")
print("-------------------------") 

# Exporting text file
Analysis_file = os.path.join("Analysis", "Analysis_data.txt")
with open(Analysis_file, "w") as outfile:
    outfile.write("Election Results\n")
    outfile.write("-------------------------\n")
    outfile.write(f"Total Votes: {total_votes}\n")
    outfile.write("-------------------------\n")
    for candidate, votes in votes_per_candidate.items():
        outfile.write(candidate + ": " + "{:.3%}".format(votes/total_votes) + " (" +  str(votes) + ")" + "\n")
    outfile.write("-------------------------\n")
    outfile.write(f"Winner: {winner}\n")
    outfile.write("-------------------------\n")
