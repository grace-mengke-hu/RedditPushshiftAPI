#!../anaconda2/bin/python

from pymongo import MongoClient

client = MongoClient() #by default the DB is on localhost
print(client.database_names())
client.drop_database('Reddit_R21')
print(client.database_names())
