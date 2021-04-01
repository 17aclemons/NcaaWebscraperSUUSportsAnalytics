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
    
with open('test.json') as f:
    data = json.load(f)

#write to a file
os.mkdir(os.getcwd() + '/Scraped')

#subset the data     
schedule = subsetDictByKey('date', data)

#write the schedule
schedule = sorted(schedule, key = lambda i: i['teamName'], reverse = False)
with open('Scraped/schedules.csv', 'a', newline = '') as file:
    writer = csv.DictWriter(file, fieldnames = list(schedule[0].keys()))
    writer.writeheader()
    for line in schedule:
        writer.writerow(line)
            
del schedule

stat = subsetDictByKey('stat', data)
stat = list(filter(lambda i: i['rank'] != 'Rank', stat))

#write the stats
stat = sorted(stat, key = lambda i: i ['teamName'], reverse = False)
with open('Scraped/stats.csv', 'a', newline = '') as file:
    writer = csv.DictWriter(file, fieldnames = list(stat[0].keys()))
    writer.writeheader()
    for line in stat:
        writer.writerow(line)
del stat


player = subsetDictByKey('team', data)
player = list(filter(lambda i: i['Jersey'] != '-', player))
player = list(filter(lambda i: i['Jersey'] != 'Jersey', player))
player = sorted(player, key = lambda i: i ['sport'], reverse = False)
#write Player stats
sports = []
for s in player:
    if s['sport'] not in sports:
        sports.append(s['sport'])

for sport in sports:
    sub = subsetDictByValue(str(sport), player)
    fileName = 'Scraped/' + str(sport) + '.csv'
    
    #find the line with the most headers
    m = -1
    for s in range(0, len(sub)):
        if len(sub[s]) > m:
            position = s
    with open(fileName, 'a', newline = '') as file:
        writer = csv.DictWriter(file, fieldnames = list(sub[position].keys()))
        writer.writeheader()
        count = 0
        for line in sub:
            #try:
                writer.writerow(line)
            #except ValueError:
                writer.writerow(line)
        

                    