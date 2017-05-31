import logging
from gensim import corpora, models, similarities

# logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

def similarity_compare(query):

    dictionary = corpora.Dictionary.load('../../tmp/deerwester.dict')
    corpus = corpora.MmCorpus('../../tmp/deerwester.mm') # comes from vecter_space_convert.py, "From strings to vectors"

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
    index.save('../../tmp/deerwester.index') # save similarity index

    sims = index[vec_lsi] # perform a similarity query against the corpus
    sims = sorted(enumerate(sims), key=lambda item: -item[1]) # calculate sorted similarity
    # print(list(enumerate(sims)))
    print(sims) # print sorted (document number, similarity score) 2-tuples

    return sims
