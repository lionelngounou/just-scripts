import fileUtil
import re

def getWordFrequencies(text):
	words = clean(text).lower().split()
	non_req = ["the","and","of","for","by","to","which","when","with","unto","things",
	"not","a","be","also","has"]
	req = ["he","his","him","i","my","me",]
	frequencies = [] ##init list of frequency tupples
	for w in words:
		if len(w)>3 or req.count(w)>0 :
			frequencies.append((w, words.count(w))) ##put them as tupples
	return sorted(set(frequencies), key=lambda tup:tup[1], reverse=True) ## remove duplicates and sort
	
def clean(text):
	return re.sub(r'[^A-Za-z]', " ", text)

def printFrequency(fileName):
	_dir = "H:\\LIONEL DEV SCRIPTS\\python\\"
	_max = 30
	lines = fileUtil.getFileLines(_dir + fileName)
	values = ''
	for x in range(len(lines)):
		values += lines[x].strip() + ' '
	##print("The lines are:::::::::>>>>>>>, ", values)
	print("The frequencies are:::>>>>>>>>> " )
	frequencies = getWordFrequencies(values)
	for i in range(len(frequencies)):
		print(frequencies[i])
		if i==_max : break

printFrequency("Words.txt")
#print(clean("Words.txthe he ;895*^!%$\"%"))
