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
collection = db['trees']
print(collection.count_documents({}))

pprint.pprint(collection.find_one().keys())#get field names of submission
pprint.pprint(collection.find_one()['comments'])
#c = collection.find_one()['comments'][0]['data']
#pprint.pprint(c)
#pprint.pprint(c[0].keys())#get field names of comment

#distinct authors and id for submissions
ids = collection.distinct('id')
_ids = collection.distinct('_id')
authors = collection.distinct('author')
print("SUBMISSION IDS AND AUTHORS:")
print(len(ids))
print(len(_ids))
print(len(authors))

#find the users for comments
#cAuthorList = []
#cIDList = []
for doc in collection.find():
	if doc['comments'] and doc['comments'][0]['data']:
		for cx in doc['comments'][0]['data']:
#			print(cx['body'])
			ids.extend(cx['author'])
			authors.extend(cx['id'])
print("SUBMISSION and comments IDS AND AUTHORS:")
mysetID = set(ids)
mysetAuthor = set(authors)
print(len(list(mysetID)))
print(len(list(mysetAuthor)))

