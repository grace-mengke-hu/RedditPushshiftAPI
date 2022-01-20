import sys
sys.path.append('C:/Users/Mengke/Dropbox/Mengke_Mike/SourceCode/RedditPushshiftAPI')
import utilFunc
import compare_fun



#load new data
prefixDir_new = 'C:/Users/Mengke/Dropbox/Mengke_Mike/Data/Data_COVID/COVID_new/'
jsonFileList_new = ['coronavirusus_Feb2020.json','coronavirusus_March2020.json','coronavirusus_April2020.json']
#['CanadaCoronavirus_Feb2020.json','CoronavirusCanada_Feb2020.json']
#['CoronavirusDownunder_Feb2020.json','CoronavirusAustralia_Feb2020.json'] 
#['CoronavirusUK_Feb2020.json']
data_new = utilFunc.loadJson(jsonFileList_new, prefixDir_new)

#load old data
prefixDir_old = 'C:/Users/Mengke/Dropbox/Mengke_Mike/Data/Data_COVID/COVID_old/'
jsonFileList_old = ['coronavirusus_Jan2Apil_2020.json']
#['CanadaCoronavirus_Jan2June2020.json','CoronavirusCanada_Jan2April2020.json']
#['CoronavirusDownunder_Jan2June2020.json','CoronavirusAustralia_Jan2June2020.json']
#['CoronavirusUK_Jan2June2020.json']
data_old = utilFunc.loadJson(jsonFileList_old, prefixDir_old)



#check utc range:
min_old,max_old = compare_fun.UTC_range(data_old)
min_new, max_new = compare_fun.UTC_range(data_new)
print('old range',min_old,max_old)
print('new range',min_new,max_new)

#checking missing data between old and new
missingData_newINold = compare_fun.check_missing_submission_newINold(data_new, data_old)
missingData_oldINnew = compare_fun.check_missing_submission_oldINnew(data_new, data_old)

print('missing new in old:',len(missingData_newINold),'missing old in new:',len(missingData_oldINnew))









