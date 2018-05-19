import json

def extract_keywords(uq):
    with open('Frequent_en_terms.json') as fjson:
        data= json.load(fjson)

    #Declare empty arrays
    word=[]
    rank=[]
    for i in range (0, len(data)):
        word.append(data[i]['Word'])
        rank.append(data[i]['Rank'])
	#split the query into individual words
    s=uq.split()  
    key_words=[]
    # set a threshold between 1-4999
    t=500 
    freq_words=[]

    if t<len(data):
        for i in range (0,t):
            freq_words.append(word[i])

    keywords=[]
    for ii in range(0, len(s)):
        if s[ii] not in freq_words:
            keywords.append(s[ii])
    return keywords
