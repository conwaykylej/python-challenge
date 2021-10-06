import os
import csv

pybank_csv = os.path.join("resources", "budget_data.csv")

# populate variable to store data

#final result variables
months_total = []
net_pl = []
average_pl = []
greatest_increase = []
greatest_decrease = []

#Variables for use within the loop but not the final analysis
monthly_difference = []
month_count =[]
greatest_month = []
lowest_month = []

#read csv file

with open(pybank_csv) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    start_row = next(csvreader)
    row = (next(csvreader))

#Set initial values for the variables
    prior_row = int(row[1])
    months_total = 1
    net_pl = int(row[1])
    greatest_increase = int(row[1])
    greatest_decrease = 0

#Go through each row with For Loop
    for row in csvreader:

        #Find Number of Months and Net Profit/Loss
        months_total += 1
        net_pl += int(row[1])
    
        #Compare and store the change from the previous month
        profit_change = int(row[1]) - prior_row
        monthly_difference.append(profit_change)
        prior_row = int(row[1])
        month_count.append(row[0])

    # Find the greatest increase

        if int(row[1]) > greatest_increase:
            greatest_increase = int(row[1])
            greatest_month = str(row[0])
    
    # Find the greatest decrease
    
        if int(row[1]) < greatest_decrease:
            greatest_decrease = int(row[1])
            lowest_month = str(row[0])
    
    #Find the average using the total monthly difference and the amount of months
    average_pl = sum(monthly_difference) / len(monthly_difference)
    average_pl = round(average_pl, 2)
    
    #fight the best and worst months using max and min
    highest = max(monthly_difference)
    lowest = min(monthly_difference)

#Print Results

print(f"Financial Analysis")
print(f"Total Months: {months_total}")
print(f"Total: ${net_pl}")
print(f"Average Change: ${average_pl}")
print(f"Greatest Increase in Profits:, {greatest_month}, (${highest})")
print(f"Greatest Decrease in Profits:, {lowest_month}, (${lowest})")


#Output finanical analysis
output_file = os.path.join("analysis", "analysis.txt")

output = (
    f"Financial Analysis\n"
    f"-----------------------------------------------\n"
    f"Total Months: {months_total}\n"
    f"Total:${net_pl}\n"
    f"Average Change: ${profit_change}\n"
    f"Greatest Increase in Profits: {greatest_month}, (${highest})\n"
    f"Greatest Decrease in Profits: {lowest_month}, (${lowest})\n"
)

#Open Output file
with open(output_file, "w") as txt_file:

    txt_file.write(output)
    
