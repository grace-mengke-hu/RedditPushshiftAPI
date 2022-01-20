import sys
sys.path.append('C:/Users/Mengke/Dropbox/Mengke_Mike/SourceCode/RedditPushshiftAPI/')
import utilFunc

prefix ='C:/Users/Mengke/Dropbox/Mengke_Mike/Data/Data_Triangulum_with_features/'

dataCig = ['cig2013-2018_proc_spacyNER_LIWC_spacyDEP.json']
dataEcig = ['e_cig2013-2018_proc_spacyNER_LIWC_spacyDEP.json']
dataMj = ['marijuana2013-2018_proc_spacyNER_LIWC_spacyDEP.json']
dataStopsmoking = ['stopsmoking2013-2018_proc_spacyNER_LIWC_spacyDEP.json']
dataTrees = ['trees_2013-2018_proc_spacyNER_LIWC_spacyDEP.json']
dataVaping101 = ['Vaping101_2013-2018_proc_spacyNER_LIWC_spacyDEP,json']
dataVaping = ['vaping2013-2018_proc_spacyNER_LIWC_spacyDEP.json']
dataWeed = ['weed2013-2018_proc_spacyNER_LIWC_spacyDEP.json']

dataAll = dataCig+dataEcig+dataMj+dataStopsmoking+dataTrees+dataVaping101+dataVaping+dataWeed

#This is too large
#loadDataAll = utilFunc.loadJson(dataAll, prefix)
print(dataAll)
    
dFile = dataEcig
currentData = utilFunc.loadJson(dFile, prefix)

userList = []
for d in currentData:#submission
    userList.append(d['author'])

currentNumUser = len(list(set(userList)))
print('unique user all data:',dFile, len(list(set(userList))))


#numList = [11824,]

#('e_cig2013-2018.json', 20248)
#('stopsmoking2013-2018.json', 32229)
#('vaping2013-2018.json', 39545)
#('marijuana2013-2018.json', 18159)
#('trees_2013-2018.json', 176359)
#('weed2013-2018.json', 1932)
#('cig2013-2018.json', 11824)
#('Vaping101_2013-2018.json', 757)
#('all users:', 301053)


