#!../anaconda2/bin/python
import json
import pickle
import random
import re

#jsonFile = 'Data_breastcancer/submission/breastcancer_all2019.json'
json13to18 = '../Data/stopsmoking2013-2018.json'
jsonList = ['stopsmoking_April2019.json',
'stopsmoking_Aug2019.json',
'stopsmoking_Feb2019.json',
'stopsmoking_Jan2019.json',
'stopsmoking_July2019.json',
'stopsmoking_June2019.json',
'stopsmoking_March2019.json',
'stopsmoking_May2019.json',
] 


pathPrefix = '../Data_EVALI/'
dataAll = []
for fp in jsonList:
	with open(pathPrefix+fp,'r') as read_file:
		data = json.load(read_file)
	dataAll = dataAll+data
with open(json13to18,'r') as read_file:
	data = json.load(read_file)
dataAll = dataAll+data

for d in dataAll:	
	dSelftext = ''
	if 'selftext' in d.keys():
		dSelftext = d['selftext']
	outText = d['title'] + '\n\n' + dSelftext

	fileName =d['author'] + '_' +str(d['created_utc']) + '_' +d['id'] +'_' +d['subreddit']


	fp = open("../cessationSubmissions/"+fileName+".txt","w")
	fp.write(outText.encode('utf-8'))
	fp.close()

		



