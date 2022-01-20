# MongoDB PROJECT
This project requires Python 2.7. It contains various scripts to manage Mongo Database.
- **mongoCheckCollection.py** checks authors and id from submission and comments from specific mongo data collection.
- **mongoDBbuild.py** builds mongo data collection from jason data, where each subreddit forms one collection and each sumission including its comments forms one document.
- **mongoDBbuildLargeComments.py** builds mongo data collection from pickle data when the data in json is too large.
- **mongoDBgridsBuild.py** is grids build collection from data with different features.
- **mongoDeletCollection.py** is to delete specific collection from database.
- **mongoDeletDB.py** is to delete specific database.
- **mongoRandomSample.py** is to randomly sample documents from specific collection and save them into pickle.
- **mongoTextExtract.py** is to extract text data from specific collection and save them into json form.
- **mongoTextTFIDF.py** is to extract text data documents from specific collection and calculate the TFIDF for entire documents.
- **mongoUpdateArchivedComments.py** is to update certain comment under specific document (ie. submission).
- **mongoDBbuildTry.py** is testing code to build collection from large data.
- **mongoTest.py** is testing code to insert document.
