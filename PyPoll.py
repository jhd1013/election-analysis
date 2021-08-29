# Compute the results of the vote and report the following:
# 1) The total number of votes cast
# 2) A complete list of candidates who received votes
# 3) The percentage of votes each candidate won
# 4) The total number of votes each candidate won
# 5) The winner of the election based on the popular vote

import csv
import os

# Setup the input and output filenames
file_to_load = os.path.join('Resources', 'election_results.csv')
file_to_save = os.path.join('analysis', 'election_analysis.txt')

# Open the input data file and process it
with open(file_to_load, "r") as election_data:
    # Create a file reader for the CSV file
    file_reader = csv.reader(election_data)
    # CSV readers get data from the CSV file row-by-row
    headers = next(file_reader)
    print(headers)
    print(file_reader.dialect.delimiter)
    

with open(file_to_save, "w") as txt_file:
    txt_file.write("Counties in the Election\n")
    txt_file.write("-------------------------\n")
    txt_file.write("Arapahoe\nDenver\nJefferson\n")
    
