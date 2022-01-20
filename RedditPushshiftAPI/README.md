# RedditPushshiftAPI PROJECT
This project contains a series of crawlers to collect Reddit data from Pushshift.io API.
- **epoch_UTC.py** contains a dictionary in the form: *\<dates in String form\>:\<UTC time in Int form\>*
- **RedditPushshiftAPI.py** is a crawler by using the UTC time frames in *epoch_utc.py*.
- **pushshift_\<month\>.py** (eg. pushshift_jan.py) are crawlers collecting data monthly by specify the subreddit and monthly time frame.
- **pushshift0.py** is crawler collecting entire data of specific subreddit from the very beginning time of the subreddit. It also checks empty subreddit.
- **pushshift0Monthly.py** is a monthly crawler. It checks empty subreddit.
- **pushshift0Yearly.py** is a yearly crawler. It checks empty subreddit.
- **pushshift\<number\>.py** (eg. pushshift1.py) are crawlers run on different machines to boost the collecting process.
- **pushshiftTestFlatComments\<number\>.py** (eg. pushshiftTestFlatComments1.py) are crawlers that flaten the comments into list form and save the entire data into json.
- **tryCrawler\<number\>.py** (eg. tryCrawler0.py) are test crawlers.
