import csv
import os
# # Open the data file.
# # Write down the names of all the candidates.
# # Add a vote count for each candidate.
# # Get the total votes for each candidate.
# # Get the total votes cast for the election.

# Assign a variable for the file to load and the path.
file_to_load = 'Resources/election_results.csv'
# # Open the election results and read the file.
# election_data = open(file_to_load, 'r')

# # To do: perform analysis.


# # Open the election results and read the file
# with open(file_to_load) as election_data:

#      # To do: perform analysis.
#      print(election_data)
#      # Close the file.
     # Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# # Using the open() function with the "w" mode we will write data to the file.
# open(file_to_save, "w")
# # Use the open statement to open the file as a text file.
# outfile = open(file_to_save, "w")
# # Write some data to the file.
# outfile.write("Hello World")# Use the open statement to open the file as a text file.


# # Close the file
# outfile.close()
# election_data.close()

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# 1. Initialize a total vote counter.
total_votes = 0
# Candidate Options
candidate_options = []
# 1. Declare the empty dictionary.
candidate_votes = {}
# candidate_votes = {"candidate_name1": votes, 
#                     "candidate_name2": votes, 
#                     "candidate_name3": votes}
# Open the election results and read the file.
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
with open(file_to_load) as election_data:
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Print the header row.
    headers = next(file_reader)
    # print(next(csv.reader(election_data)))
    print(headers)
    # Print each row in the CSV file.
    for row in file_reader:
        # 2. Add to the total vote count.
        total_votes += 1
        # Add the candidate name to the candidate list.
        #row[2] has the candidate name
        if row[2] not in candidate_options:
            candidate_options.append(row[2])
            candidate_votes[row[2]]=0
        # Add a vote to that candidate's count.
        candidate_votes[row[2]] += 1
        # print(row)
    # 3. Print the total votes.
    # print(total_votes)
    # Print the candidate list.
    # print(candidate_options)
    # Print the candidate vote dictionary.
    print(candidate_votes)
    # Determine the percentage of votes for each candidate by looping through the counts.
# 1. Iterate through the candidate list.
for candidate_name in candidate_votes:
    # 2. Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    # 3. Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100
    # 4. Print the candidate name and percentage of votes.
    #percentage is formatted to one decimal place
    print(f"{candidate_name}: received {round(vote_percentage,1)}% of the vote.")
    # Determine winning vote count and candidate
    # 1. Determine if the votes are greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        # 2. If true then set winning_count = votes and winning_percent =
        # vote_percentage.
        winning_count = votes
        winning_percentage = vote_percentage
        # 3. Set the winning_candidate equal to the candidate's name.
        winning_candidate = candidate_name
    # To do: print out each candidate's name, vote count, and percentage of
    # votes to the terminal.
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
    print(winning_candidate_summary)
