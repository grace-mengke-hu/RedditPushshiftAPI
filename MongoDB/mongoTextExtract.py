#!../anaconda2/bin/python

from pymongo import MongoClient


client = MongoClient() #open localhost port
print(client.database_names())
db = client.Reddit_R21 #get database
print(db.collection_names())

#get collection
myCol = db.weed

tmpList = []
for d in myCol.find():
	tmpDic = {}
	tmpDic['id'] = d['id']
	tmpDic['title']=d['title']
	tmpDic['comments']=d['comments']
	tmpDic['created_utc']=d['created_utc']
	tmpList.append(tmpDic)

#import pprint
#pprint(tmpList[0])

print(tmpList[0])
#print(tmpList[0]['comments'][0]['data'][0].keys())
#print(tmpList[1])

import json
with open('DataInJson/weed.json', 'w') as outfile:
	json.dump(tmpList, outfile)


