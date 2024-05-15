import os
import csv



#locate where the csv file is.
budget_data_csv = os.path.join("Resources", "budget_data.csv")

#create list for the data
months = []
profit_loss = []
changes = []

#tell program to use csv reader and seperate rows by ","
with open(budget_data_csv) as csv_file:
    csvreader = csv.reader(csv_file, delimiter=",")
    #seperate header from lists
    csv_header = next(csv_file)
    for row in csvreader:
        months.append(row[0])
        profit_loss.append(int(row[1]))
       

cleaned_csv = list(zip(months, profit_loss))

output_file = os.path.join("Resources", "py_bank_final.csv")
#create new file with cleaned 
with open(output_file, "w", newline='') as datafile:
    writer = csv.writer(datafile)
    writer.writerow(["months", "profit_loss"])
    writer.writerow(cleaned_csv)


#finding the total of the profit_loss list
total = sum(profit_loss)


#locate desired file for changes in profit/loss
cleaned_csv = os.path.join("Resources", "py_bank_final.csv")
with open(cleaned_csv) as csv_file:
    csvreader = csv.reader(csv_file, delimiter=",")
    #seperate header from lists
    csv_header = next(csv_file)
    for row in csvreader:
            #create new list to find the increase/decrease in profits
            for i in range(len(profit_loss) - 1):
                current_change = profit_loss[i]
                next_change = profit_loss[i + 1]
                change = next_change - current_change
                changes.append(int(change))
    
                                                   
#find the average change
average_change = sum(changes) / len(changes)
#find the greatest increase and decrease in profit
greatest_increase = max(changes)
greatest_decrease = min(changes)

#determine the month for the greatest increase and decrease in profits
cleaned_csv = os.path.join("Resources", "py_bank_final.csv")
with open(cleaned_csv) as csv_file:
    csvreader = csv.reader(csv_file, delimiter=",")
    #seperate header from lists
    csv_header = next(csv_file)
    for row in csvreader:
            for i in range(len(changes)):
                if changes[i] == greatest_decrease:
                    greatest_decrease_month = months[i + 1]  
                if changes[i] == greatest_increase:
                    greatest_increase_month = months[i + 1]

#print Financial Analysis
print("")
print("Financial Analysis")
print("")
print("--------------------------------------------------")
print("")
print(f'Total Months: {(int(len(months)))}')
print("")
print(f'Total: ${(total)}')
print("")
print(f'Average Change: ${round(average_change, 2)}')
print("")
print(f'Greatest Increase in Profits: {greatest_increase_month} (${int(greatest_increase)})')
print("")
print(f'Greatest Decrease in Profits: {greatest_decrease_month} (${int(greatest_decrease)})')

