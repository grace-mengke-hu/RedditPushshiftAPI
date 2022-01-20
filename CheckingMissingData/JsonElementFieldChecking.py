import sys
sys.path.append('C:/Users/Mengke/Dropbox/Mengke_Mike/SourceCode/RedditPushshiftAPI')
import utilFuncimport json

#open json file. Remark: Each json file is a list of initiating posts. Comment list is within each initiating post.
with open("../Data/Vaping101_2013-2018.json","r") as read_file:
	data = json.load(read_file)

#Going through each initiating post
for d in data[1:10]:
	#EXTRACT TEXT FOR INITIATING POST
	print("ALL FIELDS FOR INITATING POST:")
	print(d.keys())
	#extract title text
	title = d['title']
	#if the initiating post has a paragraph of text, extract that text
	#REMARK: You might need both title and selftext as the text data for initiating post.
	if 'selftext' in d.keys():
		title_selftext = d['selftext']

	#EXTRACT COMMENTS REMARK: Some initiating posts do not have follow-up comments. In that case, d['comments']=''. To extract valid comments, we need to make sure d['comments'] is non empty. 
	if d['comments']:
		#go through comment list
		for c in d['comments']:
			print("ALL FIELDS FOR EACH COMMENT:")
			print(c['data'][0].keys()) #each comment is a dictionary under c['data'][0]
			comment_body = c['data'][0]['body']

