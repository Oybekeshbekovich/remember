# Python reading files(.txt , .json, .csv)
file_path = 'C:/Users/user/Desktop/you_tube/remamber.txt'
try:
    with open(file_path, 'r') as f:
        content = f.read()
        print(content)
except FileNotFoundError:
    print("None")
# json
import json

file_path = 'C:/Users/user/Desktop/you_tube/remamber.txt'
try:
    with open(file_path, 'r') as f:
        content = json.load(f)
        print(content['Javohir'])
except FileNotFoundError:
    print("None")
# csv
import csv

file_path = 'C:/Users/user/Desktop/you_tube/remamber.txt'
try:
    with open(file_path, 'r') as f:
        content = csv.reader(f)
        for row in content:
            print(row[2])
except FileNotFoundError:
    print("None")
