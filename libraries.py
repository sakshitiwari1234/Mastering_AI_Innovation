import array

arr = array.array('i' , [1,2,3,4])

print(arr)

# random

import random

print(random.randint(1,10))


# 
import os
print(os.getcwd())

# os.mkdir('test_dir')


import shutil

shutil.copyfile('sample.txt' , 'destination.txt')


# data serialization

import json

data = {'name': 'Sakshi' , 'age' : 30}

json_Str = json.dumps(data)
print(json_Str)
print(type(json_Str))


parsed_data = json.loads(json_Str)
print(parsed_data)
print(type(parsed_data))



# csv

import csv

with open('example.csv', mode= 'w', newline= '') as file:
    writer = csv.writer(file)
    writer.writerow(['name', 'age'])
    writer.writerow(['lrish', 34])
    
with open('example.csv', mode='r') as file:
    reader  =csv.reader(file)
    for row in reader:
        print(row)
        
        

# datetime

from datetime import datetime , timedelta

now = datetime.now()
print(now)

yesterday = now-timedelta(days = 1)
print(yesterday)


# time
import time
print(time.time())

time.sleep(2)
print(time.time())

# regular expressions 

import re 
pattern = r'\d+'
text = 'there are 123 appless'
match = re.search(pattern , text)
print(match.group())

