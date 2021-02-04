import csv

#set file to variable
newValuesFile = 'newValues.csv'

#open file 
with open(newValuesFile, newline='') as csvfile:
#save file contents to object
    reader = csv.DictReader(csvfile)

    for row in reader:
        print(row['id'], row['questiontext'], row['newquestiontext'])


#Set up sql string template

#insert file object contents into string template

#save sql to new file