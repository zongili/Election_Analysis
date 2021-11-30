import csv
import os
# # Open the data file.
# # Write down the names of all the candidates.
# # Add a vote count for each candidate.
# # Get the total votes for each candidate.
# # Get the total votes cast for the election.

# # Assign a variable for the file to load and the path.
# file_to_load = 'Resources/election_results.csv'
# # Open the election results and read the file.
# election_data = open(file_to_load, 'r')

# # To do: perform analysis.


# # Open the election results and read the file
# with open(file_to_load) as election_data:

#      # To do: perform analysis.
#      print(election_data)
#      # Close the file.
#      # Create a filename variable to a direct or indirect path to the file.
# file_to_save = os.path.join("analysis", "election_analysis.txt")
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

# Open the election results and read the file.
with open(file_to_load) as election_data:
    # Read the file object with the reader function.
    # file_reader = csv.reader(election_data)

    # Print the header row.
    # headers = next(file_reader)
    print(next(csv.reader(election_data)))
    # print(headers)
    # Print each row in the CSV file.
    # for row in file_reader:
    #     print(row)
    