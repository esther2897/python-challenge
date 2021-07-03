import os
import csv
csvpath = os.path.join('..', 'Resources', 'budget_data.csv')
totalmonths = 0
netprofit = 0
difference_arr = []
past_number = 0
difference = 0
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    for row in csvreader:
        totalmonths = totalmonths + 1
        profit = row[1]
        netprofit = netprofit + profit
        difference = past_number - profit
        difference_arr.append[difference]
    max_diff = max(difference_arr)
    max_diff_index = difference_arr(max_diff) + 1
    min_diff = max(difference_arr)
    min_diff_index = difference_arr(min_diff) + 1
    r_index = 0
    for row in csvreader:
        r_index = r_index + 1
        if r_index == max_diff_index:
            max_month = row [0]
        elif r_index == min_diff_index:
            min_month = row [0]
    av_money = sum(difference_arr)/len(difference_arr)
    introline = "Financial Analysis"
    dashline = "----------------------------"
    total_line = "Total Months: " + str(totalmonths)
    total_prof_line = "Total: $" + str(netprofit)
    av_line = "Average  Change: $" + str(double(av_money))
    greatest_line = "Greatest Increase in Profits: " + max_month + " ($" + str(max_diff) + ")"
    least_line = "Greatest Decrease in Profits: " + min_month + " ($" + str(min_diff) + ")"
print (introline)
print(dashline)
print(total_line)
print(total_prof_line)
print(av_line)
print(greatest_line)
print(least_line)
output_path = os.path.join("..", "analysis", "summary.csv")
with open(output_path, 'w') as csvfile:
    # Initialize csv.writer
    csvwriter_new = csv.writer(csvfile, delimiter=',')
    csvwriter_new.writerow([introline])
    csvwriter_new.writerow([dashline])
    csvwriter_new.writerow([total_line])
    csvwriter_new.writerow([total_prof_line])
    csvwriter_new.writerow([av_line])
    csvwriter_new.writerow([greatest_line])
    csvwriter_new.writerow([least_line])
