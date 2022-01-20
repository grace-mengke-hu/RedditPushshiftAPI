#!../anaconda2/bin/python

from pymongo import MongoClient


client = MongoClient() #open localhost port
print(client.database_names())
db = client.Reddit_R21 #get database
print(db.collection_names())

treeSize = db.trees.count()
marijuanaenthusiastsSize = db.marijuanaenthusiasts.count()
Vaping101Size = db.Vaping101.count()
weedSize = db.weed.count()
CigarettesSize = db.Cigarettes.count()
eCigSize = db.electronic_cigarette.count()
marijuanaSize = db.marijuana.count()
stopsmokingSize = db.stopsmoking.count()
vapingSize = db.vaping.count()

total = treeSize+marijuanaenthusiastsSize+Vaping101Size+weedSize+CigarettesSize+eCigSize+marijuanaSize+stopsmokingSize+vapingSize
print(total)

vapingList = []
for d in db.vaping.find():
	vapingList.append(d)

print(len(vapingList))
print(db.vaping.count())

import random
import pickle
num = 15
new_list = random.sample(vapingList,num)

pickle.dump( new_list, open( "SampleRandom/vaping15.p", "wb" ) )

#num_selection = 
#my_list = [1, 2, 3, 4, 5]
#num_selections = 3
#new_list = random.sample(my_list, num_selections)
#print(my_list)
#print(new_list)
#print(db.weed.getIndexes())
