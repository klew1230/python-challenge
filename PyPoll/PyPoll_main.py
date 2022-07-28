import csv
import os

# initialize variables

ballots = {}
total_votes = 0
csvpath = os.path.join('Resources', 'election_data.csv')

#open csv file
with open(csvpath,'r') as csvfile:
    #split the data on commas
    csvreader = csv.reader(csvfile,delimiter = ',')
    # skip first line
    csv_header = next(csvreader)


    for row in csvreader:
        candidate = row[2]

        total_votes = total_votes +1

        if candidate in ballots:
            # if candidate has been seen before, add 1 vote
            ballots[candidate] = ballots[candidate] + 1
        else:
            # if new candidate, initialize candidate to 1
            ballots[candidate] = 1
    


# sort vote total values from greatest to least
votes = list(ballots.values())
votes_sorted = sorted(votes, reverse = True)
candidates = list(ballots.keys())

with open("analysis/pypoll.txt","w") as txt_file:
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------")

    txt_file.write("Election Results\n")
    txt_file.write("-------------------------\n")
    txt_file.write(f"Total Votes: {total_votes}\n")
    txt_file.write("-------------------------\n")

    # print first value in votes_sorted, match value with correct candidate
    for i in range(len(votes)):
        #stores the current vote value
        votenum = votes_sorted[i]
        #searches unsorted votes list for matching value, and stores index value as 'position'
        position = votes.index(votes_sorted[i])
        #uses 'position' index value to store candidate name as votecand
        votecand = candidates[position]
        #calculates percentage of total votes for current candidate
        percent = str(round(100 * votenum / total_votes, 3)) + "%"
        print(f"{candidates[position]:<30}:{percent:>8} ({votenum:,})")
        txt_file.write(f"{candidates[position]:<30}:{percent:>8} ({votenum:,})\n")

    print("-------------------------")
    print(f"Winner: {candidates[votes.index(votes_sorted[0])]}")
    print("-------------------------")

    txt_file.write("-------------------------\n")
    txt_file.write(f"Winner: {candidates[votes.index(votes_sorted[0])]}\n")
    txt_file.write("-------------------------\n")   
