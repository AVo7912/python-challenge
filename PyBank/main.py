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

    output_Sum = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {num_lines}\n"
    f"Total: ${sum(profit)}\n"
    f"Average Change: ${avg_change:.2f}\n"
    f"Greatest Increase in Profits: {max_change_date} (${max_change})\n"
    f"Greatest Decrease in Profits: {min_change_date} (${min_change})\n")

  print(output_Sum)