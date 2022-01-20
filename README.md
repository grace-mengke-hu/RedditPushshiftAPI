# Data Collection Package With Pushshift.io API

## RedditPushshiftAPI
This package is for all the crawlers using pushshift.io API
- **RedditPushshiftAPI.py** is the crawler for COVID dataset
- **epoch_UTC.py** provide the utc time stamp for each month
- **pushshift\*.py** files are the crawler for TRIANGULUM(marijuana, vaping, and tobacco) dataset 

## CheckingMissingData
This package is for checking missing data for the pushshift.io. We noticed that when we collect data for 6 months time frame, we lost data for some months. This happened when collecting COVID data. 


## ExtractInfo
This package is for pulling submission text(title and description), comments(body text), creating time, author, and post ID. 
 