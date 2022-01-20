import requests
import pandas as pd
import json
import time
import epoch_UTC

start_time = time.time()

def getPushshiftData(sub=None, before=None, after=None, ids=None, getSubmissions=True, getComments=False):
	suffix=''
	searchType = 'submission'
	if getComments or not getSubmissions:
		searchType='comment'
	if (before is not None):
		suffix += '&before='+str(before)
	if (after is not None):
		suffix += '&after='+str(after)
	if (sub is not None):
		suffix += '&subreddit='+sub
	if (ids is not None):
		suffix += '&ids='+','.join(ids)

	url = 'https://api.pushshift.io/reddit/search/'+searchType+'?sort=desc'+suffix
	#r = requests.get(url)
	try:
		r = requests.get(url)
		data = json.loads(r.content)
		if len(data['data']) > 0:
			prev_end_date = data['data'][-1]['created_utc']
		else:
			prev_end_date = None
	except Exception as e:
		data = []
		prev_end_date=None

	return (data, prev_end_date)
		

#given submissionID get all comment IDs for that submission
def getCommentsID(submissionID=None):
	url= "https://api.pushshift.io/reddit/submission/comment_ids/"+subID
   	# print('loading... '+url)
	#r = requests.get(url)
	try:
		r = requests.get(url)
		data = json.loads(r.content)
	except Exception as e:
		data=[]
	return data

#from comment IDs get comments
def getComments(commentIDs=None):
	comments=[]
	for id in commentIDs['data']:
		url = "https://api.pushshift.io/reddit/comment/search?ids="+id
		#r = requests.get(url)
		try:
			r = requests.get(url)
			c = json.loads(r.content)
			comments.append(c)
		except Exception as e:
			print("NO COMMENTS:")
			print(url)
	return comments

#Initialize after time stamp
timeBegin = epoch_UTC.date_utc_dic('Wednesday, July 1, 2020 12:00:00 AM')
timeEnd =   epoch_UTC.date_utc_dic('Friday, July 31, 2020 11:59:59 PM')

sub = 'coronavirusus'#'CoronavirusDownunder'#'CanadaCoronavirus'#'Covid19_USA'#'CoronavirusAustralia'#'CoronavirusUK'#'CovidUK'#'CoronavirusCanada'#'CovidCanada'#'CovidAustralia'#'CoronavirusCanada'#'CovidCanada'#'CovidUK'#'China_Flu'#'askreddit'#'ausents'#'relationship_advice'#'advice' #'ncov'#'coronavirusNY'#'coronavirusCA'#'askreddit'#'coronavirusus'#'coronavirus'#'electronic_cigarette'#'trees'#'weed'#'Vaping101'#'marijuanaenthusiasts'#'alcoholism'#'opiates'#'alcoholicsanonymous'#'alcohol'#'alcoholicsanonymous'#'alcoholism'#'cripplingalcoholism'#'marijuanaenthusiasts'#'Vaping101'#'Cigarettes'#'electronic_cigarette'#'trees'#'marijuana'#'weed'#'vaping'#'stopsmoking' #'stopdrinking'
(submissions_tmp,prev_end_date) = getPushshiftData(sub=sub,before=timeEnd,after=timeBegin)
#'1587427199'
if submissions_tmp:
	submissions = submissions_tmp['data']
else:
	submissions = []

#submissions = submissions_tmp['data']
#print(prev_end_date)#This is the earlist post within time slot
#print(len(submissions))
#print(submissions[0]["full_link"])
#print(submissions[0]["num_comments"])#comments of comments are included
while prev_end_date is not None:
	#gradually shrink the searching time slot to get missing post(This is the way to exceeding 1000 posts)
	(submissions_tmp,prev_end_date) = getPushshiftData(sub=sub, before=prev_end_date-1, after=timeBegin)
	if prev_end_date is not None:
		submissions.extend(submissions_tmp['data'])
print("number of submission:")
print(len(submissions))#number of submission increases
print(sub)


#COMMENTS
print("HERE ARE THE COMMENTS:")
for s in submissions:
	subID = s["id"]
	commentsIDs = getCommentsID(submissionID=subID)
	if commentsIDs:
		comments = getComments(commentsIDs)
	else:
		comments = []
	s["comments"]=comments
#print(submissions[0])

#submission_data["data"]=submissions
with open('C:/Users/Mengke/Dropbox/Mengke_Mike/Data/Data_COVID/COVID_new2/coronavirusus_July2020.json','w') as outfile: #('../Data/alcohol_JanToApril20_2020.json', 'w') as outfile:
	json.dump(submissions, outfile)


end_time = time.time()
print("--- %s seconds ---" % (end_time - start_time))

