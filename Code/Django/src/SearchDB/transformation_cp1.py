import logging
import os
from gensim import corpora, models, similarities

# logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

def transformation(DictPath, mmPath, LsiPath, filename):

    '''
    transform documents from one vector representation into another.
    This process serves two goals:

    1. To bring out hidden structure in the corpus,
    discover relationships between words and use them to describe the documents in a new and (hopefully) more semantic way.

    2. To make the document representation more compact.
    This both improves efficiency (new representation consumes less resources) and efficacy (marginal data trends are ignored, noise-reduction).

    '''

    if (os.path.exists(DictPath + filename + '.dict')):
        dictionary = corpora.Dictionary.load(DictPath + filename + '.dict')
        corpus = corpora.MmCorpus(mmPath + filename + '.mm')
        print("Used files generated from vecter_space_convert.py")
    else:
        print("Please generate data set")

    tfidf = models.TfidfModel(corpus) # step 1 -- initialize a model

    corpus_tfidf = tfidf[corpus] # step 2 -- use the model to transform vectors

    lsi = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=2) # initialize an LSI transformation
    corpus_lsi = lsi[corpus_tfidf] # create a double wrapper over the original corpus: bow->tfidf->fold-in-lsi

    lsi.save(LsiPath + 'model.lsi') # same for tfidf, lda, ...
