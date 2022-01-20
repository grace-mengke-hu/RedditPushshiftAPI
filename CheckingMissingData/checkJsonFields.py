#!../anaconda2/bin/python
import json
import pprint

with open("../Data_COVID/weed_Jan.json","r") as read_file:
        data = json.load(read_file)

#print(data[0]['comments'][0]['data'][0]['created_utc'])

pprint.pprint(data[0])#get all the fields' names

for d in data: #each submission
	print(d['created_utc'])
