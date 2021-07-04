import os
import csv
csvpath = os.path.join('Resources', 'election_data.csv')
total_votes = 0
candidates = []
output_path = os.path.join("analysis", "new.csv")

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

    with open(output_path, 'w') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter = ',')
        header = "Election Results"
        print(header)
        csvwriter.writerow(header)
        dashes = "-------------------------"
        print(dashes)
        csvwriter.writerow(dashes)
        total_vote_string = "Total Votes: " + str(total_votes)
        print(total_vote_string) 
        print(dashes)
        csvwriter.writerow(dashes)
        csvwriter.writerow(total_vote_string)
        votes_per_candidates = []
        for people in refined_candidates:
            votes = countingQueen(candidates, people)
            votes_per_candidates.append(votes)
            percent = votes/total_votes
            candidates_string = people + ": " + "{:.3%}".format(percent) + " (" + str(votes) + ")"
            print(candidates_string)
            csvwriter.writerow(candidates_string)
        print(dashes)
        csvwriter.writerow(dashes)
        winner_num = max(votes_per_candidates)
        winner_index = votes_per_candidates.index(winner_num)
        winner = refined_candidates[winner_index]
        winner_string = "Winner: " + winner
        print(winner_string)
        csvwriter.writerow(winner_string)
        print(dashes)
        csvwriter.writerow(dashes)


    



