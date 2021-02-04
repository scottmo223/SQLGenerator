import csv

#set file to variable
newValuesFile = 'newValues.csv'

#open file 
with open(newValuesFile, newline='') as csvfile:
    #save file contents to object
    reader = csv.DictReader(csvfile)

    #insert file object contents into string template
    for row in reader:
        if(row['newquestiontext'] == ''):
            pass
        else:
            replacementQuestion = row['newquestiontext']
            questionId = row['id']

            #Set up sql string template
            sqlString = f"update OSUSR_H0L_QUESTION set QUESTIONTEXT = '{replacementQuestion}' where id = {questionId}"
            print(sqlString)


#save sql to new file