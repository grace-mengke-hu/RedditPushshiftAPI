# Data Collection Package With Reddit Pushshift.io API
## Publications
This package is for collecting Reddit dataset for the following publications:
This package achieves the Reddit dataset collection sections for the following publications:
1. Mengke Hu and Ryzen Benson and Annie T. Chen and Shu-Hong Zhu and MikeConway, *"Determining the prevalence of cannabis, tobacco, and vaping device mentions in online communities using natural language processing"*, Drug and Alcohol Dependence, 2021, DOI: 10.1016/j.drugalcdep.2021.109016, url: https://www.sciencedirect.com/science/article/abs/pii/S0376871621005111?via=ihub  
2. Ryzen Benson and Mengke Hu and Annie T Chen and Shu-Hong Zhu and Mike Conway, *"Leveraging Reddit to Explore the Evolving Trajectories of Cannabis, Tobacco, and Vaping Device Users"*, Frontiers in Public Health, 2021
3. Mengke Hu and Mike Conway, *"Using Reddit data to investigate perspectives on the COVID-19 pandemic using natural language processing: a comparative study of the US, the UK, Canada and Australia"*, prepare to submit to JMIR on Public Health, 2022

This package was written in Python 2.7. It contains following projects:
## RedditPushshiftAPI
This project contains a series of crawlers to collect Reddit data from Pushshift.io API.
## MongoDB
This project requires Python 2.7. It contains various scripts to manage Mongo Database.
## CheckingMissingData
As Pushshift.io Reddit API sometimes failed to update the deleted sumission and comments, this project is to compare and check the two Reddit datasets from the same time period and the same subreddit but collected at the different time. 
## ExtractInfo
This project is to extract useful text data from Reddit subreddit datasets that match the requirements of different regular expression filters.
 
