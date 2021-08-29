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
file_to_save = os.path.join('analysis', 'election_results.txt')

# Open the input data file and process it
with open(file_to_load, "r") as election_data:
    # Create a file reader for the CSV file
    file_reader = csv.reader(election_data)
    # CSV readers get data from the CSV file row-by-row
    headers = next(file_reader)
    
    # Create named numbers to access each column of the CSV data
    cty_col = 1
    cand_col = 2
    total_votes = 0
    counties_votes = {}
    candidates_votes = {}
    
    for row in file_reader:
        total_votes += 1
        county_name = row[cty_col]
        if county_name not in counties_votes.keys():
            counties_votes[county_name] = 1
        else:
            counties_votes[county_name] +=1

        candidate_name = row[cand_col]
        if candidate_name not in candidates_votes.keys():
            candidates_votes[candidate_name] = 1
        else:
            candidates_votes[candidate_name] += 1

divider = "-------------------------\n"

with open(file_to_save, "w") as txt_file:
    results_message = (
        f'Election Results\n'
        f'{divider}'
        f'Total Votes: {total_votes:,}\n'
        f'{divider}\n'
        f'County Votes:\n'
    )
    txt_file.write(results_message)
    print(results_message)
    
    winning_percentage = 0
    winning_vote_count = 0
    
    winning_county = ""
    for county in counties_votes.keys():
        vote_count = counties_votes[county]
        percentage = vote_count / total_votes * 100
        results_message = f'{county}: {percentage:.1f}% ({vote_count:,})\n'
        txt_file.write(results_message)
        print(results_message)
        if (vote_count > winning_vote_count):
            winning_vote_count = vote_count
            winning_county = county
    
    results_message = (
        f'\n{divider}'
        f'Largest County Turnout: {winning_county}\n'
        f'{divider}'
    )
    txt_file.write(results_message)
    print(results_message)

    winning_candidate = ""
    winning_vote_count = 0
    winning_percentage = 0
    for candidate_name in candidates_votes:
        vote_count = candidates_votes[candidate_name]
        percentage = vote_count / total_votes * 100
        results_message = f'{candidate_name}: {percentage:.1f}% ({vote_count:,})\n'
        txt_file.write(results_message)
        print(results_message)
        if (vote_count > winning_vote_count and percentage > winning_percentage):
            winning_candidate = candidate_name
            winning_percentage = percentage
            winning_vote_count = vote_count

    results_message = (
        f'{divider}'
        f'Winner:  {winning_candidate}\n'
        f'Winning Vote Count: {winning_vote_count:,}\n'
        f'Winning Percentage: {winning_percentage:.1f}%\n'
        f'{divider}'
    )
    txt_file.write(results_message)
    print(results_message)
