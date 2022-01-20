#!../anaconda2/bin/python
import json


with open("DataInJson/AllDataProc2.json","r") as read_file:
        data = json.load(read_file)

#print(data[0]['comments'][0]['data'][0]['created_utc'])

#print(data[0])
id1 = 'do3c1fw'
id2 = 'e0ohfhr'
utc1 = 1507496729
utc2 = 1529008110
findData = []
for d in data:
	if d['comments']:
		for c in d['comments']:
			if c['data'][0]['id']== id1 and c['data'][0]['created_utc']==utc1:
				findData.append(d)
			if c['data'][0]['id']== id2 and c['data'][0]['created_utc']==utc2:
				findData.append(d)

with open('checkChunk.json', 'w') as outfile:
	json.dump(findData, outfile)			
