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

    s=uq.split()  #split the query into individual words
    key_words=[]
    t=500 # set a threshold between 1-4999
    freq_words=[]

    if t<len(data):
        for i in range (0,t):
            freq_words.append(word[i])

    keywords=[]
    for ii in range(0, len(s)):
        if s[ii] not in freq_words:
            keywords.append(s[ii])
    return keywords
