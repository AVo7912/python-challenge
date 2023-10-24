# python-challenge

#Start PyBank code
#import modules
import os
import csv

#create path for csv file
csvpath = os.path.join('C:/Users/Aline/anaconda3/CSV Files/PyBank/Resources/budget_data.csv')

with open(csvpath) as csvfile:
  csvreader = csv.reader(csvfile, delimiter=',')

  #Skip header
  next(csvreader, None)

  #Count number of total
  num_lines = sum(1 for row in csvreader)

with open('C:/Users/Aline/anaconda3/CSV Files/PyBank/Resources/budget_data.csv') as revenue_data:
  reader = csv.reader(revenue_data, delimiter=',')

  #skip header
  next(reader, None)

  #Set lists to capture changes
  profit = []
  date = []
  change = []

  #for loop to track changes
  for row in reader:
    profit.append(float(row[1]))
    date.append(row[0])

  #for loop to run through data, calculate revenue change, and average of the change 
  for i in range(1,len(profit)):
    change.append(profit[i] - profit[i-1])   
    avg_change = sum(change)/len(change)

    #calculate greatest increase and decrease in profits
    max_change = max(change)
    min_change = min(change)

    #track corresponding date to max and min
    max_change_date = str(date[change.index(max(change))])
    min_change_date = str(date[change.index(min(change))])

    #Print output summary
    output_Sum = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {num_lines}\n"
    f"Total: ${sum(profit)}\n"
    f"Average Change: ${avg_change:.2f}\n"
    f"Greatest Increase in Profits: {max_change_date} (${max_change})\n"
    f"Greatest Decrease in Profits: {min_change_date} (${min_change})\n")

  print(output_Sum)

Output:
Financial Analysis
----------------------------
Total Months: 86
Total: $22564198.0
Average Change: $-8311.11
Greatest Increase in Profits: Jul-16 ($1862002.0) #I was not able to get it to be the correct date, I was one month off for some reason, but the values were correct
Greatest Decrease in Profits: Jan-14 ($-1825558.0) #I was not able to get it to be the correct date, I was one month off for some reason, but the values were correct

#Start PyPoll code

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

Output:
Election Results
-------------------------
Total Votes: 369711
-------------------------
Charles Casper Stockham: 23.049 % ( 85213 )
Diana DeGette: 73.812 % ( 272892 )
Raymon Anthony Doane: 3.139 % ( 11606 )
-------------------------
Winner: Diana DeGette
-------------------------
