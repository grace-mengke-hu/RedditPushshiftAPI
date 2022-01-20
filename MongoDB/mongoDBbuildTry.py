#!../anaconda2/bin/python

from pymongo import MongoClient
import datetime
import json
import pprint

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
with open('../DataWfeature/trees_2013-2018_proc_spacyNER_LIWC_spacyDEP.json') as f:
	data = json.load(f)
print('lenght data',len(data))

largeData = []
for i in range(len(data)):
	try:
		result = collection.insert_one(data[i])
	except:
		largeData.append(data[i])

import pickle
pickle.dump(largeData, open( "trees_tooLarge.p", "wb" ) )
#with open('eCig_tooLarge.json', 'w') as outfile:
#        json.dump(largeData, outfile)	
#result = collection.insert_many(data[25000:26000])
#(data[21000:25000])
#(data[20000:21000])
#(data[0:20000])
#result2 = collection.insert_many(data[20000:])
#print(len(result.inserted_ids))
print('docs in collection',collection.count_documents({}))

