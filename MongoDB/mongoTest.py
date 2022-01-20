#!../anaconda2/bin/python

from pymongo import MongoClient
import datetime
import json
import pprint

client = MongoClient()

#attribute style
db = client.test_database #dictionary style db = client['test-database']
#print(collection1.count_documents({}))

collection1 = db.Marijuana_collection
collection2 = db.vaping_collection
 
print(db)
print(collection1)
print(collection2)

post = {"author": "Mike",
         "text": "My first blog post!",
         "tags": ["mongodb", "python", "pymongo"],
         "date": datetime.datetime.utcnow()}

x = collection1.insert_one(post)
print(x)
#insert a document into a collection
#posts = db.posts
#post_id = posts.insert_one(post).inserted_id
#print(post_id)
#print(db)
#print(collection1)
#print(db.collection_names(include_system_collections=False))
#pprint.pprint(posts.find_one())#find the first document from posts

#with open('../Data/vaping_2013.json') as f:
#	data = json.load(f)

#collection1.insertOne(data[0])
#print(data[0])
#x = collection1.insert_one(data[0])
#x1= collection1.insert_one(data[1])
#print(x)
#print(data[0])
print(collection1.count_documents({}))
#pprint.pprint(data[0]['title'])
#for p in collection1.find():
#	pprint.pprint(p)

#print(len(data))
