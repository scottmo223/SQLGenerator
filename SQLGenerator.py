import csv

newValuesFile = 'newValues.csv'
sqlStatements = []

#open file 
with open(newValuesFile, newline='') as csvfile:
    #save file contents to object
    reader = csv.DictReader(csvfile)

    #insert file object contents into string template
    for row in reader:
        if(row['newvalue'] == ''):
            pass
        else:
            #Set up sql string template
            replacementQuestion = row['newvalue']
            questionId = row['id']
            sqlString = f"update OSUSR_H0L_QUESTION set QUESTIONTEXT = '{replacementQuestion}' where id = {questionId}\n"

            sqlStatements.append(sqlString)

#save sql to new file
with open('sqlFile.txt', 'w') as sqlFile:
    for statement in sqlStatements:
        sqlFile.write(statement)