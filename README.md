# Election Analysis

## Project Overview
A representative from the Colorado Board of Elections has requested an audit of the vote for a recent local congression election.  The representative has asked for a report of:

1. The total number of votes cast
2. A complete list of candidates that received votes
3. The total number of votes each candidate received
4. The percentage of votes each candidate won
5. The winner of the election based on the popular vote

## Resources
- Source Data:  [election_results.csv](./Resources/election_results.csv)
- Analysis Script:  PyPoll_Challenge.py (./PyPoll_Challenge.py)
- Tools Used:  Python 3.7, Visual Studio Code
- Script Terminal Output:  [terminal_output.png](./analysis/terminal_output.png)
- Script Output File:  [election_results.txt](./analysis/election_results.txt)

## Election Audit Results
The analysis of the election data show that:
- There were 369,711 votes cast in the election
- The following candidates received votes
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane
- The results were:
    - Charles Casper Stockham received 23.0% of the vote and 38,855 votes
    - Diana DeGette received 73.8% of the vote and 272,892 votes
    - Raymon Anthony Doane received 3.1% of the vote and 11,606 votes
- The winner of the election was:
    - Diana DeGet with 73.8% of the vote (272,892 votes)

## Election Audit Summary
This same script and technique can be easily reused for any election with slight modifications.  For example:
- Modify the script to prompt the user for the location of the file to be analyzed, rather than requiring that a file be in a specific location
- Modify the script to access the elections database rather than requiring a csv file