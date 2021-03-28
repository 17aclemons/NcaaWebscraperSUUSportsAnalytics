import json
import csv

with open('data.json') as f:
    data = json.load(f)
    
for line in data:
    if('teamName' in line):
        with open('schedule.csv', 'w'):
            



