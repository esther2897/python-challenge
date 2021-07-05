import os
import csv
csvpath = os.path.join('Resources', 'budget_data.csv')
totalmonths = 0
netprofit = 0
difference_arr = []
past_number = 0
difference = 0
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    next(csvreader)
    for row in csvreader:
        totalmonths = totalmonths + 1
        profit = row[1]
        netprofit = netprofit + int(profit)
        difference = int(profit) - past_number
        past_number = int(profit)
        difference_arr.append(difference)
    difference_arr[0] = 0
    max_diff = max(difference_arr)
    max_diff_index = difference_arr.index(max_diff) + 1
    min_diff = min(difference_arr)
    min_diff_index = difference_arr.index(min_diff) + 1
    r_index = 0

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    next(csvreader)
    for row in csvreader:
        r_index = r_index + 1
        if r_index == max_diff_index:
            max_month = row [0]
        elif r_index == min_diff_index:
            min_month = row [0]
    av_money = sum(difference_arr[1:])/(len(difference_arr) - 1)
    introline = "Financial Analysis"
    dashline = "----------------------------"
    total_line = "Total Months: " + str(totalmonths)
    total_prof_line = "Total: $" + str(netprofit)
    av_line = "Average  Change: $" + str(round(av_money, 2))
    greatest_line = "Greatest Increase in Profits: " + max_month + " ($" + str(max_diff) + ")"
    least_line = "Greatest Decrease in Profits: " + min_month + " ($" + str(min_diff) + ")"
print (introline)
print(dashline)
print(total_line)
print(total_prof_line)
print(av_line)
print(greatest_line)
print(least_line)
output_path = os.path.join("analysis", "summary.txt")
with open(output_path, 'w') as summary:
    summary.write(introline)
    summary.write("\n")
    summary.write(dashline)
    summary.write("\n")
    summary.write(total_line)
    summary.write("\n")
    summary.write(total_prof_line)
    summary.write("\n")
    summary.write(av_line)
    summary.write("\n")
    summary.write(greatest_line)
    summary.write("\n")
    summary.write(least_line)
    summary.write("\n")
    summary.close()
