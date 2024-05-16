import os
import csv
import statistics



#locate where the csv file is.
election_data_csv = os.path.join("Resources", "election_data.csv")
analysis_txt = os.path.join("Analysis", "Election_Results.txt")
#create list for the data
ballot_id = []
county = []
candidates = []
Charles = []
Diana = []
Raymon = []

#tell program to use csv reader and seperate rows by ","
with open(election_data_csv) as csv_file:
    csvreader = csv.reader(csv_file, delimiter=",")
    #seperate header from lists
    csv_header = next(csv_file)
    for row in csvreader:
        ballot_id.append(row[0])
        county.append((row[1]))
        candidates.append((row[2]))

cleaned_csv = list(zip(ballot_id, county, candidates))

output_file = os.path.join("Resources", "election_data_final.csv")
#create new file with cleaned data 
with open(output_file, "w", newline='') as datafile:
    writer = csv.writer(datafile)
    writer.writerow(["ballot_id", "county", "candidates"])
    writer.writerow(cleaned_csv)

#number of total votes
total_votes = len(ballot_id)

#use cleaned data file to determine values needed
data_final_csv = os.path.join("Resources", "election_data_final.csv")
#output_file = os.path.join("election_data_final.csv")
with open(data_final_csv) as csv_file:
    csvreader = csv.reader(csv_file, delimiter=",")
    #seperate header from lists
    csv_header = next(csv_file)
    for row in csvreader:
        for i in range(len(ballot_id)):
                if candidates[i] == "Charles Casper Stockham": 
                    Charles.append(ballot_id)
                if candidates[i] == "Diana DeGette": 
                    Diana.append(ballot_id)
                if candidates[i] == "Raymon Anthony Doane": 
                    Raymon.append(ballot_id)

#determine the number of votes each candidate received                
charles_vote = len(Charles)
diana_vote = len(Diana)
raymon_vote = len(Raymon)

#find percentage of the votes each candidate received
charles_vote_percent = (charles_vote /total_votes)* 100
diana_vote_percent = (diana_vote/total_votes)* 100
raymon_vote_percent = (raymon_vote/total_votes) * 100
#cleaned up decimal point display
rounded_charles = round(charles_vote_percent, 3)
rounded_diana = round(diana_vote_percent, 3)
rounded_raymon = round(raymon_vote_percent, 3)

#used mode to determine the winner
from statistics import mode
winner = mode(candidates)

results_data = (
                f"Election Results\n"
                f"-----------------------------------------\n"
                f'Total Votes: {total_votes}'
                f"-----------------------------------------\n"
                f'Charles Casper Stockham: {rounded_charles}%  ({charles_vote})\n'
                f'Diana Degette: {rounded_diana}%  ({diana_vote})\n'
                f'Raymon Anthony Doane: {rounded_raymon}%  ({raymon_vote})\n'
                f"-----------------------------------------\n"
                f'Winner: {winner}\n'
                )

print(results_data)

with open(analysis_txt, 'w') as txt_file:
     txt_file.write(results_data)


#print results
