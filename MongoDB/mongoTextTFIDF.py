#!../anaconda2/bin/python

from pymongo import MongoClient


client = MongoClient() #open localhost port
print(client.database_names())
db = client.Reddit_R21 #get database
print(db.collection_names())

#get different text document from collections
marijuanaCol = db.marijuana
marijuanaDocs = []
for d in marijuanaCol.find():
	marijuanaDocs.append(d['title'])
	if d['comments']: #check if there is any comments for current submission
		for c in d['comments']: 
			marijuanaDocs.append(c['data'][0]['body'])	
print('number of documents in marijuana collection:',len(marijuanaDocs))

vapingCol = db.vaping
vapingDocs = []
for d in vapingCol.find():
	vapingDocs.append(d['title'])
	if d['comments']: #check if there is any comments for current submission
		for c in d['comments']:
			vapingDocs.append(c['data'][0]['body'])
print('number of documents in vaping collection:',len(vapingDocs))

stopsmokingCol = db.stopsmoking
stopsmokingDocs = []
for d in stopsmokingCol.find():
	stopsmokingDocs.append(d['title'])
	if d['comments']: #check if there is any comments for current submission
		for c in d['comments']:
			stopsmokingDocs.append(c['data'][0]['body'])
print('number of documents in stopsmoking collection:',len(stopsmokingDocs))

ecigCol = db.electronic_cigarette
ecigDocs = []
for d in ecigCol.find():
	ecigDocs.append(d['title'])
	if d['comments']: #check if there is any comments for current submission
		for c in d['comments']:
			ecigDocs.append(c['data'][0]['body'])
print('number of documents in ecig collection:',len(ecigDocs))

cigCol = db.Cigarettes
cigDocs = []
for d in cigCol.find():
	cigDocs.append(d['title'])
	if d['comments']: #check if there is any comments for current submission
		for c in d['comments']:
			cigDocs.append(c['data'][0]['body'])
print('number of documents in cig collection:',len(cigDocs))

weedCol = db.weed
weedDocs = []
for d in weedCol.find():
	weedDocs.append(d['title'])
	if d['comments']: #check if there is any comments for current submission
		for c in d['comments']:
			weedDocs.append(c['data'][0]['body'])
print('number of documents in weed collection:',len(weedDocs))


Vaping101Col = db.Vaping101
Vaping101Docs = []
for d in Vaping101Col.find():
	Vaping101Docs.append(d['title'])
	if d['comments']: #check if there is any comments for current submission
		for c in d['comments']:
			Vaping101Docs.append(c['data'][0]['body'])
print('number of documents in Vaping101 collection:',len(Vaping101Docs))


mjEnthusiastCol = db.marijuanaenthusiasts
mjEnthusiastDocs = []
for d in mjEnthusiastCol.find():
	mjEnthusiastDocs.append(d['title'])
	if d['comments']: #check if there is any comments for current submission
		for c in d['comments']:
			mjEnthusiastDocs.append(c['data'][0]['body'])
print('number of documents in mjEnthusiast collection:',len(mjEnthusiastDocs))

treeCol = db.trees
treeDocs = []
for d in treeCol.find():
	treeDocs.append(d['title'])
	if d['comments']: #check if there is any comments for current submission
		for c in d['comments']:
			treeDocs.append(c['data'][0]['body'])
print('number of documents in tree collection:',len(treeDocs))


#for d in marijuanaCol.find():
#	print(d)
#"""
#myCol: input collection from database
#return list of documents; each document is one comment text or submission body text.
#"""
#def getDocs(myCol):
#	docs = []
#	for d in myCol.find():
#		title = d['title']
#		docs.append(title)
#		print(d)
#		if d['comments']: #check if there is any comments for current submission
#			for c in d['comments']:
#				docs.append(c['data'][0]['body'])
#				print(c['data'][0]['body'])
#		
#		return docs
			

#extract text data as document
#marijuanaDocs = getDocs(marijuanaCol)
#print(marijuanaDocs)
#vapingDocs = getDocs(vapingCol)
#stopsmokingDocs = getDocs(stopsmokingCol)
#ecigDocs = getDocs(ecigCol)
#cigDocs = getDocs(cigCol)
#weedDocs = getDocs(weedCol)
#Vaping101Docs = getDocs(Vaping101Col)
#mjEnthusiastDocs = getDocs(mjEnthusiastCol)
#treeDocs = getDocs(treeCol)

AllDocs = marijuanaDocs+vapingDocs+stopsmokingDocs+ecigDocs+cigDocs+weedDocs+Vaping101Docs+mjEnthusiastDocs+treeDocs 
#numDocs = len(AllDocs)
print("the total number of comments and submission titles:",len(AllDocs))

#TF IDF calculation
print("start TF transform")
from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(AllDocs)
featureNames = vectorizer.get_feature_names()
vocabulary = vectorizer.vocabulary_ 
idf = vectorizer.idf_
print('feature names for entire database:',len(featureNames),len(vocabulary))

#save
import pickle

fp = open('Keywords/TFIDF.p','wb')
pickle.dump(X,fp)
fp.close()

fp = open('Keywords/featureNames.p','wb')
pickle.dump(featureNames,fp)
fp.close()

fp = open('Keywords/vocabulary.p','wb')
pickle.dump(vocabulary,fp)
fp.close()

fp = open('Keywords/idf.p','wb')
pickle.dump(idf,fp)
fp.close()



