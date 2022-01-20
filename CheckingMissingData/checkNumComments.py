#!../anaconda2/bin/python
import json

#pull out json for those random authors
with open("../rawAlldata.json","r") as read_file:
	dataAll = json.load(read_file)

numC = []
for d in dataAll:
	if d['comments']:
		numC.append(len(d['comments']))
	else:
		numC.append(0)

numC.sort(reverse = True)

numG20 = 0
for n in numC:
	if n>=20:
		numG20 =numG20+1

print(numC[:20])
print(len(numC),numG20)




