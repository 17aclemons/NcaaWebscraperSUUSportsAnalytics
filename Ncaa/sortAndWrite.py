import json
import csv
import os

scheduleCount = 0
statsCount = 0
psCount = 0

with open('data.json') as f:
    data = json.load(f)

os.mkdir(os.getcwd() + '\Webscraper')

f = open('Webscraper\schedule.csv', 'w')
f.close()
f = open('Webscraper\stats.csv', 'w')
f.close()
f = open('Webscraper\schedule.csv', 'w')
f.close()

for line in data:
    if 'date' in line:
        field_names = list(line.keys())
        with open('Webscraper/schedule.csv', 'a') as schedule:
            if scheduleCount == 0:
                writer = csv.DictWriter(schedule, fieldnames = field_names)
                writer.writeheader()
                writer.writerow(line)
                scheduleCount += 1
            else:
                writer.writerow(line)
    elif 'stat' in line:
        field_names = list(line.keys())
        with open('Webscraper/stats.csv', 'a') as stats:
            if statsCount == 0:
                writer = csv.DictWriter(stats, fieldnames = field_names)
                writer.writeheader()
                writer.writerow(line)
                statsCount += 1
            else:
                writer.writerow(line)
    elif 'team':
        field_names = list(line.keys())
        with open('Webscraper/playerStats.csv', 'a') as ps:
            if psCount == 0:
                writer = csv.DictWriter(ps, fieldnames = field_names)
                writer.writeheader()
                writer.writerow(line)
                psCount += 1
            else:
                writer.writerow(line)