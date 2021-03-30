import json
import csv
import os

def subsetDictByKey(key):
    subset = []
    for line in data:
        if key in list(line.keys()):
            subset.append(line)
    return subset

with open('test.json') as f:
    data = json.load(f)

#subset the data dict and remove it from the original    
schedule = subsetDictByKey('date')
stat = subsetDictByKey('stat')

#write to a file
os.mkdir(os.getcwd() + '/Scraped')

#write the schedule
schedule = sorted(schedule, key = lambda i: i['teamName'], reverse = False)
with open('Scraped/schedules.csv', 'a', newline = '') as file:
    writer = csv.DictWriter(file, fieldnames = list(schedule[0].keys()))
    writer.writeheader()
    for line in schedule:
        writer.writerow(line)
del schedule

#write the stats
stat = sorted(stat, key = lambda i: i ['teamName'], reverse = False)
with open('Scraped/stats.csv', 'a', newline = '') as file:
    writer = csv.DictWriter(file, fieldnames = list(stat[0].keys()))
    writer.writeheader()
    for line in stat:
        writer.writerow(line)
del stat

#write Player stats
#teamNames and the sport in a list
teamNames = []
sports = []
for line in data:
    try:
        if line['teamName'] not in teamNames:
            teamNames.append(line['teamName'])
        if line['sport'] not in sports:
            sports.append(line['sport'])
    except KeyError:
        print()

for sport in sports:
    for team in teamNames:
        fileName = 'Scraped/' + str(sport) + str(team) + '.csv'
        with open(fileName, 'a') as file:
            count = 0
            for line in data:
                if team in line and sport in line:
                    if count == 0:
                        writer = csv.DictWriter(file, fieldnames = list(line.keys()))
                        writer.writeheader()
                        count += 1
                    else:
                        writer.writerow(line)
            count == 0
                    
        
        
#subset in a list 
