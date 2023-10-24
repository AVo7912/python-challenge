#import modules
import os
import csv

#print title
print("Election Results")
print("-------------------------")

#create path for csv file
csvpath = os.path.join('C:/Users/Aline/anaconda3/CSV Files/PyPoll/Resources/election_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #Skip header
    next(csvreader, None)

    #Count number of total votes
    num_lines = sum(1 for row in csvreader)
    print("Total Votes:", num_lines)
    print("-------------------------")
    
#open path to read as content file
with open('C:/Users/Aline/anaconda3/CSV Files/PyPoll/Resources/election_data.csv', 'r') as content_file:
    content = content_file.read()

    #Calculate numbers, percent, and print values for Charles Casper Stockham
    CCSNum = content.count("Charles Casper Stockham")
    CCSPercent = round((content.count("Charles Casper Stockham")/num_lines) * 100, 3)
    print("Charles Casper Stockham:", CCSPercent, "%", "(",CCSNum,")")

    #Calculate numbers, percent, and print values for Diana DeGette
    DDNum = content.count("Diana DeGette")
    DDPercent = round((content.count("Diana DeGette")/num_lines) * 100, 3)
    print("Diana DeGette:", DDPercent, "%", "(",DDNum,")")

    #Calculate numbers, percent, and print values for Raymon Anthony Doane
    RADNum = content.count("Raymon Anthony Doane")
    RADPercent = round((content.count("Raymon Anthony Doane")/num_lines) * 100, 3)
    print("Raymon Anthony Doane:", RADPercent, "%", "(",RADNum,")")
    print("-------------------------")

    #Calculate winner
    #create list of votes for each candidate
    Candidates = [CCSNum, DDNum, RADNum]

    #if statement to determine who has the highest amount of votes and print winners name
    if max(Candidates) == CCSNum:
        print("Winner: Charles Casper Stockham")

    elif max(Candidates) == DDNum:
        print("Winner: Diana DeGette")

    else:
        print("Winner: Raymon Anthony Doane")
    print("-------------------------")
