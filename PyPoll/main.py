import os
import csv
csvpath = os.path.join('Resources', 'election_data.csv')
total_votes = 0
candidates = []
output_path = os.path.join("analysis", "summary_election.txt")

def countingQueen(list, value):
    count = 0
    for element in list:
        if element == value:
            count += 1
    return count

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    next(csvreader)

    for row in csvreader:
        total_votes = total_votes + 1
        candidates.append(row[2])
    refined_candidates = list(dict.fromkeys(candidates))
    percent = 0
    votes = 0

with open(output_path, 'w') as summary_election:
    header = "Election Results"
    print(header)
    summary_election.write(header)
    summary_election.write("\n")
    dashes = "-------------------------"
    print(dashes)
    summary_election.write(dashes)
    summary_election.write("\n")
    total_vote_string = "Total Votes: " + str(total_votes)
    print(total_vote_string) 
    summary_election.write(total_vote_string)
    summary_election.write("\n")
    print(dashes)
    summary_election.write(dashes)
    summary_election.write("\n")
    votes_per_candidates = []
    for people in refined_candidates:
        votes = countingQueen(candidates, people)
        votes_per_candidates.append(votes)
        percent = votes/total_votes
        candidates_string = people + ": " + "{:.3%}".format(percent) + " (" + str(votes) + ")"
        print(candidates_string)
        summary_election.write(candidates_string)
        summary_election.write("\n")
    print(dashes)
    summary_election.write(dashes)
    summary_election.write("\n")
    winner_num = max(votes_per_candidates)
    winner_index = votes_per_candidates.index(winner_num)
    winner = refined_candidates[winner_index]
    winner_string = "Winner: " + winner
    print(winner_string)
    summary_election.write(winner_string)
    summary_election.write("\n")
    print(dashes)
    summary_election.write(dashes)
    summary_election.write("\n")
    summary_election.close()


    



