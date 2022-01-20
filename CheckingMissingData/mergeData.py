import sys
sys.path.append('C:/Users/Mengke/Dropbox/Mengke_Mike/SourceCode/RedditPushshiftAPI/')
import utilFunc

prefix_old = 'C:/Users/Mengke/Dropbox/Mengke_Mike/Data/Data_COVID/COVID_merge/'
#'C:/Users/Mengke/Dropbox/Mengke_Mike/Data/Data_COVID/COVID_old/'
prefix_new = 'C:/Users/Mengke/Dropbox/Mengke_Mike/Data/Data_COVID/COVID_new2/'
#'C:/Users/Mengke/Dropbox/Mengke_Mike/Data/Data_COVID/COVID_new/'
prefix_merge = 'C:/Users/Mengke/Dropbox/Mengke_Mike/Data/Data_COVID/COVID_merge/'
#'C:/Users/Mengke/Dropbox/Mengke_Mike/Data/Data_COVID/COVID_merge/'

#file list by country
US_old = ['coronavirusus_Feb2Nov_2020_update.json']
#['coronavirusus_Feb2Nov_2020.json'] 
#[ 'coronavirusus_Jan2Apil_2020.json',
#          'coronavirusus_May2June2020.json',
#          'coronavirusus_July2Oct2020.json']

Canada_old = ['CanadaCoronavirus_Jan2June2020.json',
            'CanadaCoronavirus_July2Oct2020.json',
            'CoronavirusCanada_Jan2April2020.json',
            'CoronavirusCanada_May2June2020.json',
            'CoronavirusCanada_July2Oct2020.json']

UK_old = ['CoronavirusUK_Feb2Nov_2020.json']
#['CoronavirusUK_Jan2June2020.json',
#        'CoronavirusUK_July2Oct2020.json']

Australia_old = [ 'CoronavirusAustralia_Jan2June2020.json',
                 'CoronavirusAustralia_July2Oct2020.json', 
                 'CoronavirusDownunder_Jan2June2020.json',
                 'CoronavirusDownunder_July2Oct2020.json']

US_new = ['coronavirusus_July2020.json']
#['coronavirusus_Aug1-Aug7_2020.json',
 #         'coronavirusus_Aug7-Aug15_2020.json',
 #         'coronavirusus_Aug15_to_Aug22_2020.json',
 #         'coronavirusus_Aug22-Aug31_2020.json',]
#[ 'coronavirusus_April2020.json',
#          'coronavirusus_Aug2020.json',
#          'coronavirusus_Feb2020.json',
#          'coronavirusus_July2020.json',
#          'coronavirusus_June2020.json',
#          'coronavirusus_March2020.json',
#          'coronavirusus_May2020.json',
#          'coronavirusus_Nov2020.json',
#          'coronavirusus_Oct2020.json',
#          'coronavirusus_Sept2020.json']

Canada_new = [ 'CoronavirusCanada_April2020.json',
              'CoronavirusCanada_Aug2020.json',
              'CoronavirusCanada_Feb2020.json',
              'CoronavirusCanada_July2020.json',
              'CoronavirusCanada_June2020.json',
              'CoronavirusCanada_March2020.json',
              'CoronavirusCanada_May2020.json',
              'CoronavirusCanada_Nov2020.json',
              'CoronavirusCanada_Oct2020.json',
              'CoronavirusCanada_Sept2020.json',
              'CanadaCoronavirus_April2020.json',
              'CanadaCoronavirus_Aug2020.json',
              'CanadaCoronavirus_Feb2020.json',
              'CanadaCoronavirus_July2020.json',
              'CanadaCoronavirus_June2020.json',
              'CanadaCoronavirus_March2020.json',
              'CanadaCoronavirus_May2020.json', 
              'CanadaCoronavirus_Nov2020.json',
              'CanadaCoronavirus_Oct2020.json',
              'CanadaCoronavirus_Sept2020.json']

Australia_new = [ 'CoronavirusAustralia_April2020.json',
                 'CoronavirusAustralia_Aug2020.json',
                 'CoronavirusAustralia_Feb2020.json',
                 'CoronavirusAustralia_July2020.json',
                 'CoronavirusAustralia_June2020.json',
                 'CoronavirusAustralia_March2020.json',
                 'CoronavirusAustralia_May2020.json',
                 'CoronavirusAustralia_Nov2020.json',
                 'CoronavirusAustralia_Oct2020.json',
                 'CoronavirusAustralia_Sept2020.json',
                 'CoronavirusDownunder_April2020.json',
                 'CoronavirusDownunder_Aug2020.json',
                 'CoronavirusDownunder_Feb2020.json',
                 'CoronavirusDownunder_July2020.json',
                 'CoronavirusDownunder_June2020.json',
                 'CoronavirusDownunder_March2020.json',
                 'CoronavirusDownunder_May2020.json',
                 'CoronavirusDownunder_Nov2020.json',
                 'CoronavirusDownunder_Oct2020.json',
                 'CoronavirusDownunder_Sept2020.json']

UK_new = ['CoronavirusUK_July2020_update.json']
#[ 'CoronavirusUK_April2020.json',
#          'CoronavirusUK_Aug2020.json',
#          'CoronavirusUK_Feb2020.json',
#          'CoronavirusUK_July2020.json',
#          'CoronavirusUK_June2020.json',
#          'CoronavirusUK_March2020.json',
#          'CoronavirusUK_May2020.json',
#          'CoronavirusUK_Nov2020.json',
#          'CoronavirusUK_Oct2020.json',
#          'CoronavirusUK_Sept2020.json'
#    ]


#read in data
data_old = utilFunc.loadJson(UK_old, prefix_old)
data_new = utilFunc.loadJson(UK_new, prefix_new)
data_merge = data_new
## add data that is in old set but not in the new
#get id list from the new data
id_new_list = []
for d in data_new:
    id_new_list.append(d['id'])
#add missing data from old data
for d in data_old: #submissions
    id_old = d['id']
    if not(id_old in id_new_list):
        data_merge.append(d)


import json
with open(prefix_merge+'CoronavirusUK_Feb2Nov_2020_update2.json','w') as outfile:
    json.dump(data_merge, outfile)



  