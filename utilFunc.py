import json
import nltk;nltk.download('stopwords')
from nltk.corpus import stopwords

def loadJson(jsonList,prefixDir):
	data = []
	for f in jsonList:
		with open(prefixDir+f) as fp:
			data = data+json.load(fp)
	return data



def userList(data):
	userList = []
	for d in data:
		userList.append(d['author'])
		if d['comments']:
			for c in d['comments']:
				userList.append(c['data'][0]['author'])
	return list(set(userList))

#initiating posts
def textData(data):
	textList = []
	for d in data:
		outText = d['title']+' '
		if 'selftext' in d.keys():
			outText = outText+d['selftext']
		textList.append(outText)
	return textList

#utc of post and user name including comments
def utc_userList(data):
	timeList = []
	userList = []
	for d in data:
		timeList.append(d['created_utc'])
		userList.append(d['author'])
		if d['comments']:
			for c in d['comments']:
				timeList.append(c['data'][0]['created_utc'])
				userList.append(c['data'][0]['author'])
	return timeList, userList


def utc_weekly_bin():
	weekBin = [1581206400,
		1581811200,
		1582416000,
		1583020800,
		1583625600,
		1584230400,
		1584835200,
		1585440000,
		1586044800,
		1586649600,
		1587254400,	
		1587859200,
		1588464000,
		1589068800,
		1589673600,
		1590278400,
		1590883200,
		1591488000,
		1592092800,
		1592697600,
		1593302400,
		1593907200,
		1594512000,
		1595116800,
		1595721600,
		1596326400,
		1596931200,
		1597536000,
		1598140800,
		1598745600,
		1599350400,
		1599955200,
		1600560000,
		1601164800,
		1601769600,
		1602374400,
		1602979200,
		1603584000,
		1604102400
	]
	return weekBin

def utc_weekly_label():
	weekLabel = ['02-09',
		'02-16',
		'02-23',
		'03-01',
		'03-08',
		'03-15',
		'03-22',
		'03-29',
		'04-05',
		'04-12',
		'04-19',
		'04-26',
		'05-03',
		'05-10',
		'05-17',
		'05-24',
		'05-31',
		'06-07',
		'06-14',
		'06-21',
		'06-28',
		'07-05',
		'07-12',
		'07-19',
		'07-26',
		'08-02',
		'08-09',
		'08-16',
		'08-23',
		'08-30',
		'09-06',
		'09-13',
		'09-20',
		'09-27',
		'10-04',
		'10-11',
		'10-18',
		'10-25',
		'10-31'
	]
	return weekLabel

def numUserInBin(weekBin, userList, timeList):
	numUserInBinList = []
	for i in range(len(weekBin)-1):
		currentBinUser = set()
		for j in range(len(timeList)):
			if timeList[j]>=weekBin[i] and timeList[j]<=weekBin[i+1]:
				currentBinUser.add(userList[j])
	
		numUserInBinList.append(len(currentBinUser))
	return numUserInBinList


def stopwords(d): #d is element in data from json pulled from pushshiftio
	#stop words
	stop_words = stopwords.words('english')
	stop_words.extend(['hi','www','com','s','http','https','amp','ampersand','from', 'subject', 're', 'edu', 'use', 'not', 'would', 'say', 'could', '_', 'be', 'know', 'good', 'go', 'get', 'do', 'done', 'try', 'many', 'some', 'nice', 'thank', 'think', 'see', 'rather', 'easy', 'easily', 'lot', 'lack', 'make', 'want', 'seem', 'run', 'need', 'even', 'right', 'line', 'even', 'also', 'may', 'take', 'come',
#extend function words to be removed https://www.edu.uwo.ca/faculty-profiles/docs/other/webb/essential-word-list.pdf
'the','which','still','although','forty','and','up','last','past','nobody','of','out','being','himself','unless','to','would','must','seven','mine','a','when','another','eight','anybody','I','your','between','along','till','in','will','might','round','herself','you','their','both','several','twelve','that','who','five','someone','fifteen','it','some','four','whatever','beyond','for','two','around','among','whom','he','because','while','across','below','on','how','each','behind','none','we','other','under','million','nor','they','could','away','outside','more','be','our','every','nine','most','with','into','next','thousand','this','these','anything','shall','have','than','few','myself','but','any','though','themselves','as','where','since','itself','not','over','against','somebody','at','back','second','upon','what','first','nothing','thirty','so','much','without','third','there','down','during','above','or','its','six','therefore','one','should','enough','everybody','by','after','once','towards','from','those','however','thus','all','may','half','everyone','she','something','yet','near','no','three','whether','inside','his','little','everything','nineteen','do','many','until','yourself','can','why','hundred','fifty','if','before','within','whose','about','such','ten','anyone','my','off','twenty','per','her','through','either','except' ])

	return stop_words	


def commonTopic():
	"""
	return list of common Topics
	"""
	return [#'Transimission risk',
'Work/Finance',#'QA',
'Social distancing&Transmission risk',
'Case report&interaction with medical system',
'Covid Testing&Vaccine&Mental Health&Scientific research',
'Policy&QA&News&Travel restriction',#'interaction with medical system',#'Travel restriction',
'Education/Children',#'Scientific research',#'News',#'Vaccine',#'Mental Health'
]

def annotateUStopic():
	"""
	return a dictionary: {LDA topic ID: annotated topic}
	"""
	UStopicMap = {
1:'Work/Finance',
2: 'Policy&QA&News&Travel restriction',#'Policy',
3:'Case report&interaction with medical system',#'interaction with medical system',
4:'Work/Finance',
5:'Social distancing&Transmission risk',#'Social distancing',
6:'Case report&interaction with medical system',#'Case report',
7:'Policy&QA&News&Travel restriction',#'QA',
8:'Covid Testing&Vaccine&Mental Health&Scientific research',#'Mental Health',
11:'Education/Children',
12:'Social distancing&Transmission risk',#'Social distancing',
13:'Case report&interaction with medical system',#'Case report',
}
	return UStopicMap 

def annotateUKtopic():
	"""
	return a dictionary: {LDA topic ID: annotated topic}
	"""
	UKtopicMap = {0:'Covid Testing&Vaccine&Mental Health&Scientific research',#'Vaccine',
2:'Education/Children',
3:'Case report&interaction with medical system',#'interaction with medical system',
4:'Policy&QA&News&Travel restriction',#'Travel restriction',
5:'Policy&QA&News&Travel restriction',#'News',
6:'Social distancing&Transmission risk',#'Social distancing',
7:'Work/Finance',
9:'Case report&interaction with medical system',#'Case report',
11:'Case report&interaction with medical system',#'Case report',
13:'Work/Finance',
15:'Covid Testing&Vaccine&Mental Health&Scientific research',#'Covid Testing',
16:'Case report&interaction with medical system',#'Case report',
18:'Case report&interaction with medical system',#'Case report',
19:'Work/Finance',
}
	return UKtopicMap

def annotateAUStopic():
	AUStopicMap = {
0:'Social distancing&Transmission risk',#'Transimission risk',
1:'Case report&interaction with medical system',#'Case report',
2:'Work/Finance',
3:'Covid Testing&Vaccine&Mental Health&Scientific research',#'Covid Testing',
4:'Case report&interaction with medical system',#'Case report',
5:'Policy&QA&News&Travel restriction',#'Travel restriction',
6:'Case report&interaction with medical system',#'Case report',
7:'Policy&QA&News&Travel restriction',#'News',
8:'Covid Testing&Vaccine&Mental Health&Scientific research',#'Scientific research',
9:'Education/Children'
}
	return AUStopicMap

def annotateCANtopic():
	CANtopicMap = {
0:'Policy&QA&News&Travel restriction',#'Travel restriction',
1:'Case report&interaction with medical system',#'Case report',
2:'Social distancing&Transmission risk',#'Social distancing',
3:'Case report&interaction with medical system',#'Case report',
4:'Covid Testing&Vaccine&Mental Health&Scientific research',#'Covid Testing',
5:'Social distancing&Transmission risk',#'Social distancing',
6:'Covid Testing&Vaccine&Mental Health&Scientific research',#'Covid Testing',
7:'Policy&QA&News&Travel restriction',#'Travel restriction',
8:'Social distancing&Transmission risk',#'Transimission risk',
9:'Education/Children',
11:'Case report&interaction with medical system',#'Case report',
12:'Covid Testing&Vaccine&Mental Health&Scientific research',#'Scientific research',
13:'Policy&QA&News&Travel restriction',#'Policy',
14:'Work/Finance'
}
	return CANtopicMap


















