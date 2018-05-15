import logging
import re
from gensim import corpora, models, similarities


# logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

def year_similarity_compare(query, txt, DictPath, mmPath, indexPath, filename):
    dictionary = corpora.Dictionary.load(DictPath + filename + '.dict')
    corpus = corpora.MmCorpus(mmPath + filename + '.mm') # comes from vecter_space_convert.py, "From strings to vectors"
    
    '''
    for i in range(0, 10):
        print corpus[i]
        print dictionary[i]
    '''

    lsi = models.LsiModel(corpus, id2word=dictionary, num_topics=2)

    doc = query
    vec_bow = dictionary.doc2bow(doc.lower().split())
    vec_lsi = lsi[vec_bow] # convert the query to LSI space

    index = similarities.MatrixSimilarity(lsi[corpus]) # transform corpus to LSI space and index it
    index.save(indexPath + filename + '.index') # save similarity index

    years = index[vec_lsi] # perform a similarity query against the corpus
    years_enu = []
    # Transform tuple data structure to list data structure and replace id to exact filename
	
    for i in range(0,len(years)):
        datepat = re.compile(r'\d+')
        year = datepat.findall(txt[i])
        year = int(year[0])
        years_enu.append([txt[i], years[i],year])
    years_enu = sorted(years_enu, key=lambda item: -item[2]) # calculate sorted similarity
    # print(list(enumerate(sims)))
    #print(sims) # print sorted (document number, similarity score) 2-tuples
    
    # THRESHOLD
    years_thres_adjust = []
    for element in years_enu:
        if element[1] > 0.5:
            element[1] = round(element[1], 2)
            years_thres_adjust.append(element)
            
    return years_thres_adjust

