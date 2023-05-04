import os, csv

#Get csv path
csvpath = os.path.join("Resources", "budget_data.csv")

#declare variables for totalMonths, netTotalAmount, averageTotalAmount
totalMonths, netTotalAmount, averageTotalAmount=(0,0,0)

#Function to Create a map; to map date to greatestChange
def createColObj():
    return {
    "date": "",
    "greatest": 1,
    } 

#function to output our final result
def dataToString():
        return f'Financial Analysis\n----------------------------\nTotal Months: {totalMonths}\nTotal: ${netTotalAmount}\nAverage Change: ${averageTotalAmount:.2f}\nGreatest Increase in Profits: {greatestIncrease["date"]} (${greatestIncrease["greatest"]})\nGreatest Decrease in Profits: {greatestDecrease["date"]} (${greatestDecrease["greatest"]})'

#Declare our greatestChange maps
greatestIncrease= createColObj()
greatestDecrease = createColObj() 

#Open csv file to begin reading
with open(csvpath,encoding='utf-8') as csvfile:
    #Assign reader and specify delimiter
    reader = csv.reader(csvfile, delimiter=',')
    #Skip label row, but store the value
    header = next(csvfile)
    for row in reader:
        #Get profit amt
        amt = int(row[1])
        #Get date
        date = str(row[0])
        #Sum profit total
        netTotalAmount+=amt
        #Each row is a distinct month, so add 1
        totalMonths+=1
        #If profit amt is greater than current greatestIncrease record it in our greatestIncrease map
        if amt > greatestIncrease["greatest"]:
            greatestIncrease["greatest"] = amt
            greatestIncrease["date"] = date
        #Else if profit amt is less than current greastestDecrease record it in our greatestDecrease map
        elif amt < greatestDecrease["greatest"]:
            greatestDecrease["greatest"] = amt
            greatestDecrease["date"] = date
    #Average Change over the months
    averageTotalAmount = netTotalAmount / totalMonths
    
#Call output function for final string
print(dataToString())

#Create output file
output_file = os.path.join("Analysis", "analysis.txt")

#Write to output
with open(output_file, "w" ) as datafile:
    #Call output function to write to our text file
     datafile.write(dataToString())
