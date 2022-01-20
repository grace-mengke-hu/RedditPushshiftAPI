#!../anaconda2/bin/python

from pymongo import MongoClient
import datetime
import json
import pprint

client = MongoClient() #open localhost port
db = client.Reddit_R21 #get database

print(db.collection_names())
mycol = db["electronic_cigarette"]
print('docs in collection',mycol.count_documents({}))
mycol.drop()
print(db.collection_names())
