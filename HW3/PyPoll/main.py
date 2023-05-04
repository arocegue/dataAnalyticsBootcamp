import os, csv

#Create Candidates Map, map candidate to votes
candidates = {}

#Path to csv file
csvpath = os.path.join("Resources", "election_data.csv")

#finalStringOutput combines results for a clean final output
finalStringOutput = ""

#open csv file to begin reading
with open(csvpath, encoding="UTF-8") as csvfile:
    #Assign reader and specify delimiter
    reader = csv.reader(csvfile, delimiter=',')
    #Skip label row, but store the value
    header = next(csvfile)
    for row in reader:
        #if row[0] is null, not a valid row (missing ballot ID)
        if row[0] is not None:
            #if candidate is not in our list, create an instance with initial vote
            if row[2] not in candidates:
                candidates[str(row[2])] = 1
            else:
                #else add vote to respective candidate
                candidates[str(row[2])] +=1
    #sum up the votes
    totalVotes = sum(candidates.values())
    #concat output
    finalStringOutput += f'Election Results\n-------------------------\nTotal Votes: {totalVotes}\n-------------------------\n'

    #create a winner obj to keep track
    winner = {"Candidate": "", "Votes": 0}

    #Iterate through candidates to tally votes, percentage and decide winner
    for candidate, votes in candidates.items():
        #if candidate votes are greater than current stored winner..replace
        if(votes > winner["Votes"]):
            winner["Votes"] = votes
            winner["Candidate"] = candidate
        finalStringOutput += f'{candidate}: {100*(votes/totalVotes):.03f}% ({votes})\n'

    #concat output
    finalStringOutput += f'-------------------------\nWinner: {winner["Candidate"]}\n-------------------------'

    #print final string
    print(finalStringOutput)

    #Create output text file
    output_file = os.path.join("Analysis", "analysis.txt")

#Write to file
with open(output_file, "w" ) as datafile:
     datafile.write(finalStringOutput)