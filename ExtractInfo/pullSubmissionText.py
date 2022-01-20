#!../anaconda2/bin/python
import json
import pickle
import random
import re


jsonList =[
'../Data_COVID/COVID/advice_Jan2Apil_2020.json',
'../Data_COVID/COVID/askreddit_Jan2Apil_2020.json',
'../Data_COVID/COVID/coronavirusCA_Jan2Apil_2020.json',
'../Data_COVID/COVID/coronavirus_Jan2Apil_2020.json',
'../Data_COVID/COVID/coronavirusNY_Jan2Apil_2020.json',
'../Data_COVID/COVID/coronavirusus_Jan2Apil_2020.json',
'../Data_COVID/COVID/ncov_Jan2Apil_2020.json',
'../Data_COVID/COVID/relationship_advice_Jan2Apil_2020.json',
'../Data_COVID/COVID/advice_May2June2020.json',
'../Data_COVID/COVID/askreddit_May2June2020.json',
'../Data_COVID/COVID/coronavirusCA_May2June2020.json',
'../Data_COVID/COVID/coronavirus_May2June2020.json',
'../Data_COVID/COVID/coronavirusNY_May2June2020.json',
'../Data_COVID/COVID/coronavirusus_May2June2020.json',
'../Data_COVID/COVID/ncov_May2June2020.json',
'../Data_COVID/COVID/relationship_advice_May2June2020.json'
] 
#['alcohol_2019.json',
#'cannabis_2019.json',
#'cripplingalcoholism_2019.json',
#'leaves_2019.json',
#'marijuana_2019.json',
#'opiates_2019.json',
#'OpiatesRecovery_2019.json',
#'Petioles_till2019.json',
#'stopdrinking_2019June.json',
#'stopdrinking_2019march.json',
#'stopdrinking_2019May.json',
#'stopdrinking_2019Nov.json',
#'stopdrinking_2019Oct.json',
#'stopdrinking_2019Sept.json',
#'stopdrinking_2019April.json',
#'stopdrinking_2019Aug.json',
#'stopdrinking_2019Dec.json',
#'stopdrinking_2019feb.json',
#'stopdrinking_2019jan.json',
#'stopdrinking_2019July.json',
#'trees_April2019.json',
#'trees_Aug2019.json',
#'trees_Dec2019.json',
#'trees_Feb2019.json',
#'trees_Jan2019.json',
#'trees_July2019.json',
#'trees_June2019.json',
#'trees_March2019.json',
#'trees_May2019.json',
#'trees_Nov2019.json',
#'trees_Oct2019.json',
#'trees_Sep2019.json']


from datetime import datetime

#timestamp = 1545730073
#dt_object = datetime.fromtimestamp(timestamp)

covidPattern = "(\W|^)covid(\W|$)|(\W|^)corona(\W|$)"

#providerPattern = "(\W|^)doctor(\W|$)|(\W|^)nurse(\W|$)|(\W|^)clinician(\W|$)|(\W|^)physician(\W|$)|(\W|^)therapist(\W|$)|(\W|^)social\sworker(\W|$)|(\W|^)psychologist(\W|$)"

#stigmaPattern = "(\W|^)shame(\W|$)|(\W|^)loser(\W|$)|(\W|^)failure(\W|$)|(\W|^)disappoint(\W|$)|(\W|^)weak(\W|$)|(\W|^)lazy(\W|$)|(\W|^)inadequate(\W|$)|(\W|^)untrustworthy(\W|$)|(\W|^)blame(\W|$)|(\W|^)hopeless(\W|$)"

pathPrefix = '../Data_COVID/'#'../Data_AnnieGrant/'
dataAll = []
for fp in jsonList:
	with open(pathPrefix+fp,'r') as read_file:
		data = json.load(read_file)
	dataAll = dataAll+data

for d in dataAll:	
	dSelftext = ''
	if 'selftext' in d.keys():
		dSelftext = d['selftext']
	outText = d['title'] + '\n\n' + dSelftext

	fileName =d['author'] + '_' +str(datetime.fromtimestamp(d['created_utc'])) + '_' +d['id'] +'_' +d['subreddit']


	if re.search(covidPattern, outText, re.IGNORECASE):    	
		fp = open(pathPrefix+"Submission/"+fileName+".txt","w")
		fp.write(outText.encode('utf-8'))
		fp.close()

		



