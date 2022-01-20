#!../anaconda2/bin/python

from pymongo import MongoClient
import datetime
import json
import pprint
import gridfs

client = MongoClient()

#create database Reddit_R21 at localhost
db = client.Reddit_R21 #dictionary style db = client['test-database']
#print(collection1.count_documents({}))

fs = gridfs.GridFS(db)

##create collection "vaping","stopsmoking" under Reddit_R21 database
#collection = db['electronic_cigarette']
 
print(db)
print(db.collection_names())
#print(collection)


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
with open('../DataWfeature/e_cig2013-2018_proc_spacyNER_LIWC_spacyDEP.json') as f:
	data = json.load(f)
print('lenght data',len(data))

for i in range(len(data)):
	a = fs.put(data[i])
#	result = collection.insert_one(data[i])
#result = collection.insert_many(data[25000:26000])
#(data[21000:25000])
#(data[20000:21000])
#(data[0:20000])
#result2 = collection.insert_many(data[20000:])
#print(len(result.inserted_ids))
#print('docs in collection',collection.count_documents({}))
print(db.collection_names())
