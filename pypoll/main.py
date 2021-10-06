import os
import csv

poll_csv = os.path.join('resources','election_data.csv')

votes = 0
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0

#Read csv file
with open(poll_csv, 'r') as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)

    for row in csvreader:

        votes +=1

        if (row[2] == "Khan"):
            khan_votes +=1
        elif (row[2] == "Correy"):
            correy_votes +=1
        elif (row[2] == "Li"):
            li_votes +=1
        else:
            otooley_votes +=1
    

    #calculate percentage of votes from number of votes and format as percentage
    kahn_percentage = khan_votes/votes
    kahn_percentage = "{:.0%}".format(kahn_percentage)

    correy_percentage = correy_votes/votes
    correy_percentage = "{:.0%}".format(correy_percentage)

    li_percentage = li_votes/votes
    li_percentage = "{:.0%}".format(li_percentage)

    otooley_percentage = otooley_votes/votes
    otooley_percentage = "{:.0%}".format(otooley_percentage)

    victor = max(khan_votes, correy_votes, li_votes, otooley_votes)

    if victor == khan_votes:
        victor_name = "Khan"
    elif victor == correy_votes:
        victor_name = "Correy"
    elif victor == li_votes:
        victor_name = "Li"
    elif victor == otooley_votes:
        victor_name = "O'Tooley"

#Print Election Results and percentages
print(f"Election Results")
print(f"----------------------------------")
print(f"Total Votes Counted: {votes}")
print(f"-----------------------------------")
print(f"Khan: {kahn_percentage}({khan_votes})")
print(f"Correy: {correy_percentage}({correy_votes})")
print(f"Li: {li_percentage}({li_votes})")
print(f"O'Tooley: {otooley_percentage}({otooley_votes})")
print(f"-----------------------------------")
print(f"And the Winner is: {victor_name}!")
print(f"-----------------------------------")
    
#Output Election Results
output_file = os.path.join("analysis", "analysis.txt")

#Create the output contents for the writing command
output = (
    f"Election Results\n"
    f"-----------------------------------------------\n"
    f"Total Votes Counted: {votes}\n"
    f"-----------------------------------------------\n"
    f"Khan: {kahn_percentage}({khan_votes})\n"
    f"Correy: {correy_percentage}({correy_votes})\n"
    f"Li: {li_percentage}({li_votes})\n"
    f"O'Tooley: {otooley_percentage}({otooley_votes})\n"
    f"-----------------------------------------------\n"
    f"And the Winner is: {victor_name}!\n"
    f"-----------------------------------------------\n"
)

#Open Output file
with open(output_file, "w") as txt_file:

    txt_file.write(output)