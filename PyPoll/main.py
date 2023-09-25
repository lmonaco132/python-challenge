# import os and csv
import os
import csv

# set up path to csv file
csvpath = os.path.join('Resources', 'election_data.csv')

# create list of strings for output later
# for now just add the header strings
analysis_out = ["Election Results", "------------"]

# open the file as a csv file
with open(csvpath) as csvfile:
    # specify the delimiter as comma and put contents into a variable
    csvreader = csv.reader(csvfile, delimiter=',')

    # read the header row
    csv_header = next(csvreader)

    # set up counter variable for number of votes cast, starting at 0 (this will count rows in csvfile)
    ballot_count = 0

    # set up dict to hold candidate names and votes (names will be keys, list of num of votes and % of votes will be values)
    candidates = {}

    # loop through the rows of csv file 
    for row in csvreader:
        # increment the ballout count to count the current vote in total
        ballot_count = ballot_count + 1

        # now we want to add the current vote to the correct candidate's count
        # we need to check if the candidate is in the set of candidates yet
        if row[2] not in candidates.keys():
            # this is the case where the candidate is not in the dictionary yet
            # add the current candidate as a key, value is 1 (number of votes we've counted for them)
            # value is a list because we're going to add the percent of votes cast for this candidate to this list after the for loop
            candidates[row[2]] = [1]
        else:
            # this is the case where the candidate is in the dictionary already
            # so we can access their vote count by using their name as the key
            # we want to add 1 to their current vote count, to count the current vote
            candidates[row[2]][0] = candidates[row[2]][0] + 1

    # now after the for loop we add the number of votes cast to the list of strings for output
    analysis_out.append(f'Total Votes Cast: {ballot_count}')
    analysis_out.append("------------")

    # set up variable to hold current highest vote-count and winner
    # start highest vote count at 0, we will find something higher than this in the list (also add string as placeholder spot for name)
    winner_votes = [0, " "]

    # iterate through the items in the dictionary of candidates
    for can in candidates:
        # calculate percent of votes received for this candidate as num of votes / total votes, append this value to the list
        candidates[can].append( candidates[can][0] / ballot_count )

        # write the current candidate's percent and total vote counts to strings for output
        analysis_out.append(f'{can}: {candidates[can][1]:.3%} ({candidates[can][0]})')

        # check if the current candidate's vote count is higher than the current winner's vote count
        if winner_votes[0] < candidates[can][0]:
            # this is the case where the current candidate has more votes than the stored maximum
            # update the winner to be the current candidate (first item in list is vote count, second is candidate name)
            winner_votes[0] = candidates[can][0]
            winner_votes[1] = can
    
    # append the winner name to the list of strings for output
    analysis_out.append("------------")
    analysis_out.append(f'Winner: {winner_votes[1]}')
    analysis_out.append("------------")
        
    
# now we have all values for output, need to set up file to write to
with open('analysis.txt', 'w') as f:
    # loop through the list of strings for output, for each one write it to the output file and print to command line

    for line in analysis_out:
        # write current string to analysis file, followed by newline
        f.write(line)
        f.write('\n')

        # print current string to the commandline
        print(line)