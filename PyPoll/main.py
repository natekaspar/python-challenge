import os
import csv

# Path for election data csv file
election_csv_file_path = "/Users/natekaspar/Desktop/python-challenge/PyPoll/Resources/election_data.csv"

# Setting the Variables

# Candidates
candidates = []
candidate_votes = {}

# Set total_votes to 0
total_votes = 0

# Open the election data CSV file
with open(election_csv_file_path, "r") as election_csvfile:
    election_csvreader = csv.reader(election_csvfile, delimiter=',')

    # Skipping first row
    header = next(election_csvreader)

    # Loop through data 
    for row in election_csvreader:
        total_votes += 1
        candidate_name = row[2]

        if candidate_name not in candidates:
            candidates.append(candidate_name)
        if candidate_name in candidate_votes:
            candidate_votes[candidate_name] += 1
        else:
            candidate_votes[candidate_name] = 1

# Getting the winner 
winner = max(candidate_votes, key=candidate_votes.get)

# Printing the results 
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
print("List of Candidates:")
for candidate in candidates:
    votes = candidate_votes[candidate]
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes} votes)")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Calculate the total number of votes
voteTotal = sum(candidate_votes.values())

# Define the output folder path where you want to save the file
TxtPath = "/Users/natekaspar/Desktop/python-challenge/PyPoll/Analysis"

# M
os.makedirs(TxtPath, exist_ok=True)

# Specify the output file path within the folder
output_file_path = os.path.join(TxtPath, "election_results.txt")

# Text file
with open(output_file_path, "w", newline='') as electionfile:
    electionfile.write(
        f"Election Results\n"
        f"-------------------------\n"
        f"Total Votes: {voteTotal}\n"
        f"-------------------------\n")

    for key, value in candidate_votes.items():
        percentage = (value / voteTotal) * 100
        electionfile.write(f"{key}: {percentage:.3f}% ({value})\n")

    electionfile.write(
        f"-------------------------\n"
        f"Winner: {winner}\n"
        f"-------------------------")
