import json
import csv
import os

def subsetDictByKey(key, js):
    subset = []
    for line in js:
        if key in list(line.keys()):
            subset.append(line)
    return subset

def subsetDictByValue(value, js):
    subset = []
    for line in js:
        if value in list(line.values()):
            subset.append(line)
    return subset

def writeFile(fileLocation, jsList):
    with open(fileLocation, 'a', newline = '') as file:
        writer = csv.DictWriter(file, fieldnames = list(jsList[0].keys()))
        writer.writeheader()
        for line in jsList:
            writer.writerow(line)
        
def sortData(keyName, jsList):
    temp = sorted(jsList, key = lambda i: i[keyName], reverse = False)
    return temp

def filterData(keyName, value, jsList):
    temp = list(filter(lambda i: i[keyName] != value, jsList))
    return temp

#read the json file
with open('data.json') as f:
    data = json.load(f)

#write to a file
os.mkdir(os.getcwd() + '/Scraped')

#subset the data     
schedule = subsetDictByKey('date', data)

#filter schedule
schedule = sortData('teamName', schedule)

#write schedule
writeFile('Scraped/schedules.csv', schedule)


#subset stats from data
stat = subsetDictByKey('stat', data)

#filter  and sort stat
stat = filterData('rank', 'Rank', stat)
stat = sortData('teamName', stat)

#write stats
writeFile('Scraped/stats.csv', stat)




#need to write team summary stats
team = subsetDictByKey('team', data)

#filter for just team stats
team = list(t for t in team if t['Jersey'] =='-')

#sort
team = sortData('year', team)

sports = []
for s in team:
    if s['sport'] not in sports:
        sports.append(s['sport'])
        
for sport in sports:
    sub = subsetDictByValue(str(sport), team)
    fileName = 'Scraped/' + str(sport) + 'TeamStats.csv'
    
    head = []
    head = {k for d in sub for k in d.keys()}
    
    with open(fileName, 'a', newline = '') as file:
        writer = csv.DictWriter(file, fieldnames = head)
        writer.writeheader()
        for line in sub:
            writer.writerow(line)

#sub player stats from data
player = subsetDictByKey('team', data)
#remove team stat table
player = filterData('Jersey', '-', player)
player = filterData('Jersey', 'Jersey', player)
#sort player
player = sortData('sport', player)

#write Player stats
sports = []
for s in player:
    if s['sport'] not in sports:
        sports.append(s['sport'])

for sport in sports:
    sub = subsetDictByValue(str(sport), player)
    fileName = 'Scraped/' + str(sport) + '.csv'
    
    #get all the keys in a list
    head = []
    head = {k for d in sub for k in d.keys()}

    with open(fileName, 'a', newline = '') as file:
        writer = csv.DictWriter(file, fieldnames = head)
        writer.writeheader()
        for line in sub:
            writer.writerow(line)
            

                    