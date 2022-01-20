#!../anaconda2/bin/python
import json
import pickle
import random
import re
import csv

jsonList = ['cripplingalcoholism_2019.json',
'leaves_2019.json',
'opiates_2019.json',
'OpiatesRecovery_2019.json',
'stopdrinking_2019June.json',
'stopdrinking_2019march.json',
'stopdrinking_2019May.json',
'stopdrinking_2019Nov.json',
'stopdrinking_2019Oct.json',
'stopdrinking_2019Sept.json',
'stopdrinking_2019April.json',
'stopdrinking_2019Aug.json',
'stopdrinking_2019Dec.json',
'stopdrinking_2019feb.json',
'stopdrinking_2019jan.json',
'stopdrinking_2019July.json']

#jsonList = ['alcohol_2019.json',
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

pathPrefix = '../Data_AnnieGrant/'

labels = ["addict","crackhead","junkie","abuser","alcoholic","criminal","felon","sinner","drunk","boozer","dope\sfiend","pothead","stoner","drug\sinjector","drug\suser","loser","failure"]
otherKeywords = ["relapse","rock\sbottom","dangerous","unpredictable","embarrass","shame","bias","prejudice","disappoint","weak","lazy","inadequate","untrustworthy","blame","hopeless","stereotype","judg","discrimin","worthless"]

labelPattern = ""
otherKeyPattern = ""

for label in labels:
	labelPattern += "(\W)" + label + "(\W)|"

for otherKeyword in otherKeywords:
	otherKeyPattern +=  otherKeyword + "|"

stigmaPattern = labelPattern + otherKeyPattern[:-1]
#stigmaPattern = "(\W|^)shame(\W|$)|(\W|^)loser(\W|$)|(\W|^)failure(\W|$)|(\W|^)disappoint(\W|$)|(\W|^)weak(\W|$)|(\W|^)lazy(\W|$)|(\W|^)inadequate(\W|$)|(\W|^)untrustworthy(\W|$)|(\W|^)blame(\W|$)|(\W|^)hopeless(\W|$)"

#old keywords list
#stigmaPattern = "shame|loser|failure|disappoint|weak|lazy|inadequate|untrustworthy|blame|hopeless|bias|prejudice|stereotype|judg|discrimin|worthless"

##add new keywords
#stigmaPattern = "addict|crackhead|junkie|abuser|alcoholic|criminal|felon|sinner|drunk|boozer|dope\sfiend|relapse|rock\sbottom|pothead|stoner|drug\sinjector|drug\suser|dangerous|unpredictable|embarrass|shame|loser|failure|disappoint|weak|lazy|inadequate|untrustworthy|blame|hopeless|bias|prejudice|stereotype|judg|discrimin|worthless"

dataAll = []
for fp in jsonList:
	with open(pathPrefix+fp,'r') as read_file:
		data = json.load(read_file)
	dataAll = dataAll+data

dicList = []
for d in dataAll:	
	dSelftext = ''
	if 'selftext' in d.keys():
		dSelftext = d['selftext']
	outText = d['title'] + '\n\n' + dSelftext

	
	fileName =d['author'] + '_' +str(datetime.fromtimestamp(d['created_utc'])) + '_' +d['id'] +'_' +d['subreddit']


	if re.search(stigmaPattern, outText, re.IGNORECASE):    	
		tmpDic = {}
		tmpDic['author'] = d['author']
		tmpDic['time'] = datetime.fromtimestamp(d['created_utc'])
		tmpDic['id'] = d['id']
		tmpDic['subreddit'] = d['subreddit']
		text = outText.strip('\n').strip('\r').encode('ascii', 'ignore')
		tmpDic['Text'] = text
		dicList.append(tmpDic)


		fp = open(pathPrefix+"stigmaNew2/"+fileName+".txt","w")
		fp.write(outText.encode('utf-8'))
		fp.close()

		



