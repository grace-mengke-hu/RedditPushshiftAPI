#!../anaconda2/bin/python

from pymongo import MongoClient
import datetime
import json
import pprint
import pickle

client = MongoClient()

#create database Reddit_R21 at localhost
db = client.Reddit_R21 #dictionary style db = client['test-database']
#print(collection1.count_documents({}))

#create collection "vaping","stopsmoking" under Reddit_R21 database
collection = db['trees']
 
print(db)
print(collection)


#x = collection1.insert_one(post)
#print(x)
#insert a document into a collection
#posts = db.posts
#post_id = posts.insert_one(post).inserted_id
#print(post_id)
#print(db)
#print(collection1)
#print(db.collection_names(include_system_collections=False))
#pprint.pprint(posts.find_one())#find the first document from posts
#2018nov.json
data = pickle.load( open( "trees_tooLarge.p", "rb" ) )
print('lenght data',len(data))

for d in data:
	if d['comments']:
		for c in d['comments']:
			result = collection.insert_one(c)

	d['comments'] = "out"
	result = collection.insert_one(d)

#for i in range(len(data)):
#	result = collection.insert_one(data[i])
#result = collection.insert_many(data[25000:26000])
#(data[21000:25000])
#(data[20000:21000])
#(data[0:20000])
#result2 = collection.insert_many(data[20000:])
#print(len(result.inserted_ids))
print('docs in collection',collection.count_documents({}))

