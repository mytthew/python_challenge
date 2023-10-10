import csv, os
from pathlib import Path

# Upload our ELection_Data CSV File
csvfile = "Resources/election_data.csv"

# Output File
outputfile = "Analysis/vote_analysis.txt"

# Establish our Parameters 
total_votes = 0
list_of_candidates = []
candidate_votes = {}
winner = ""
winning_number_of_votes = 0

#Read the CSV - DictReader was Used Here to Help Convert the Data Into a List of Dictionaries 
with open(csvfile) as ElectionData:
    csvreader =  csv.DictReader(ElectionData)

    for row in csvreader:

        total_votes = total_votes + 1

        # Extract all the Candidates Names 
        candidate_name = row["Candidate"]

        # And Check to see if the Candidate is Already in our List of Canidates
        if candidate_name not in list_of_candidates:

            list_of_candidates.append(candidate_name)

            candidate_votes[candidate_name] = 0

        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

with open(outputfile, "w") as txt_file:    

    # Determine the Total Number of Votes
    election_outcome = (
        f"\n\nFinal Election Results\n"
        f"------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"------------------------\n"
    )
    print(election_outcome)

    # Save the Total Number of Votes to out Text File
    txt_file.write(election_outcome)

    # For Loop to Help us Determine the Winner 
    for candidate in candidate_votes:

        votes = candidate_votes.get(candidate)
        percent_of_votes = float(votes) / float(total_votes) * 100

        # Determine the Winner
        if (votes > winning_number_of_votes):
                winning_number_of_votes = votes
                winner = candidate

        # Determine Every Candidate's Total Number of Votes and Percentage of Total Votes 
        voter_info = f"{candidate}: {percent_of_votes:.1f}% ({votes})\n"
        print(voter_info)

        txt_file.write(voter_info)

    # Determine the Winner 
    winner_summary = (
        f"--------------------\n"
        f"Winner: {winner}\n"
        f"--------------------\n"
    )
    print(winner_summary)

    # Save Winner's Info to the Text File
    txt_file.write(winner_summary)







