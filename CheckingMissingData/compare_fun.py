#give json data within certain range, find all the titles written by the same author
def check_submission_author(submission_author,data):
	titleList = []
	for d in data:
		if d['author'] == submission_author:
			titleList.append(d['title'])
	return titleList

def check_comment_author(comment_author,data):
	bodyList = []
	for d in data:
		if d['comments']:#check if comment list is empty
			for c in d['comments']:
				if c['data'][0]['author']==comment_author:
					bodyList.append(c['data'][0]['body'])
	return bodyList
	

#check if new data can be found in old data
def check_missing_submission_newINold(data_new, data_old):		
	missingData = []
	for d_new in data_new:
		id_new = d_new['id']
		ind = 0
		for d_old in data_old:
			if d_old['id'] == id_new:				
				print('=== OK FIND IT!!! ===')
				ind = 1
		if ind==0:#missing
			missingData.append(d_new)
	return missingData

#check if old data can be found in new data
def check_missing_submission_oldINnew(data_new, data_old):
	missingData = []
	for d_old in data_old:
		id_old = d_old['id']
		ind = 0
		for d_new in data_new:
			if d_new['id'] == id_old:
				print('=== OK FIND IT!!! ===')
				ind = 1
		if ind==0:#missing
			missingData.append(d_old)
	return missingData

#given json data, find the starting time and ending time from the submissions
def UTC_range(data):
	utcList = []
	for d in data:
		utcList.append(d['created_utc'])
	return min(utcList),max(utcList)




