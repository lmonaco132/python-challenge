#import os and csv
import os
import csv

# set up the path from current folder to the csv file
csvpath = os.path.join('Resources', 'budget_data.csv')

# create a list of strings for printing later
# add the header strings to start, more will be added later
analysis_out = ['Financial Analysis', '------------']

# open the file as a csv file
with open(csvpath) as csvfile:
    # specify delimiter and put contents into variable
    csvreader = csv.reader(csvfile, delimiter=',')

    # read the header row
    csv_header = next(csvreader)

    # set up variables for net profit and number of months
    # we will find these by looping through the rows of the csv file
    # both should start at 0 since they're running totals
    net_profit = 0
    month_count = 0

    # we also want to look at the change in profit for each month 
    # we'll store the previous row's profit/loss to be able to reference when looking at the next row
    # to start with set this to 0
    prev_profit = 0
    # and we'll store all the changes in profits in a list (need both value and date, so it'll be list of list)
    profit_change = []

    # loop through the rows of the csv file
    for row in csvreader:
        # add the current row's profit to the running total
        net_profit = net_profit + int(row[1])

        # check if we're on the first row (month count would still be 0)
        if month_count == 0:
            prev_profit = int(row[1])
            # this is the case where we're at the first row
            # we can't know the change in profit for the first row because we don't know profit from before the data (obviously)
            # need to set prev_profit to the current profit so it's ready for next iteration

        else:
            # this is the case where month count was Not 0, meaning it was set in the previous iteration
            # we need to store this row in the profit change list: first value is the date from the current row
            # second value is the current row's profit minus the previous profit (this is the change)
            profit_change.append( [row[0], int(row[1]) - prev_profit ] )

            # now we update prev_profit to be this row's profit so it's ready for next iteration
            prev_profit = int(row[1])

        # update the month count
        month_count = month_count + 1


    # add number of months (which we counted as number of rows) to the list of output strings
    analysis_out.append("Total Months: " + str(month_count))

    # after the for loop, we have the net profit, and a list of the changes from month to month
    # add total profit to the list of strings for output 
    analysis_out.append("Total: $" + str(net_profit))

    # now to find max and min change, and calculate average change, we need to loop through list of changes by month
    # set up holder variables for the largest and smallest change (these will be updated as we loop through the list)
    # to start we set these to be the first row of the list of lists 
    max_change = profit_change[0]
    min_change = profit_change[0]

    # also set up a variable to hold running total of changes, this will be used to calculate average change
    change_total = 0
    

    for row in profit_change:
        # add current change to the running total for average calculation
        change_total = change_total + row[1]

        # we want to check if current change is greater than current max or smaller than current min
        if (max_change[1] < row[1]):
            # this is the case where the current change is greater than max change
            # update max change to be this row
            max_change = row

        if (min_change[1] > row[1]):
            # this is the case where the current change is less than min change
            # update min change to be this row
            min_change = row
        
    # now after the for loop, we have max and min change, and the total of the changes
    # to calculate the average change, divide total changes by number of months (number of rows in profit_change)
    # append calculated average change to the list of strings for output (formatted to only show 2 decimal places)
    analysis_out.append(f'Average Change: ${change_total / len(profit_change):.2f}')

    # also add the max and min changes to the list of strings for output
    analysis_out.append(f'Greatest Increase in Profits: {max_change[0]} ${max_change[1]}')
    analysis_out.append(f'Greatest Decrease in Profits: {min_change[0]} ${min_change[1]}')


# now we have all values for output, we need to set up file to write to
with open('analysis.txt', 'w') as f:
    # now we want to write each line of the output list to the file as well as print to the commandline
    # so we'll loop through the analysis output list

    for line in analysis_out:
        # write current string to the analysis file, followed by newline
        f.write(line)
        f.write('\n')

        # print current string to the commandline
        print(line)
    



        
    