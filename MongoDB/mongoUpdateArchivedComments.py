#!../anaconda2/bin/python

from pymongo import MongoClient
import datetime
import json
import pprint


client = MongoClient() #open localhost port
print(client.database_names())
db = client.Reddit_R21 #get database
print(db.collection_names())

#name of collections: 'vaping'
collection = db['vaping']
print(collection.count_documents({}))

#sub = collection.find_one()
#c = sub['comments'][0]['data']
#pprint.pprint(sub.keys())#get field names of submission
#pprint.pprint(sub)
#pprint.pprint(c)
#pprint.pprint(c[0].keys())#get field names of comment
#trees_combine_all_records.txt
with open('../Data/archivedComments_vaping.json') as f:
        data = json.load(f)
print("archived")
pprint.pprint(data[0]['data'][0])
print(len(data))

print(data[0]['data'][0]['link_id'])
#print(sub['id'])

	
notFindList = []
for d in data:
	link_id = d['data'][0]['link_id'].replace('t3_','')
	doc = collection.find_one({"id":link_id})
	if doc:
		comments = doc['comments']

		#start updating comments
		comments.append(d)
		collection.update(
		{'_id': doc['_id']},
		{"$set":{'comments':comments}}
		)
	#print(len(collection.find_one({"id":link_id})['comments']))
	else:
		notFindList.append(d)
		print("not find")
if notFindList:
	print(len(notFindList))
	with open('VapingNotInsert.json', 'w') as outfile:
        	json.dump(notFindList, outfile)
