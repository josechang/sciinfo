import logging
import os
from gensim import corpora, models, similarities

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

'''
transform documents from one vector representation into another.
This process serves two goals:

1. To bring out hidden structure in the corpus,
discover relationships between words and use them to describe the documents in a new and (hopefully) more semantic way.

2. To make the document representation more compact.
This both improves efficiency (new representation consumes less resources) and efficacy (marginal data trends are ignored, noise-reduction).

'''

if (os.path.exists("../tmp/deerwester.dict")):
    dictionary = corpora.Dictionary.load('../tmp/deerwester.dict')
    corpus = corpora.MmCorpus('../tmp/deerwester.mm')
    print("Used files generated from vecter_space_convert.py")
else:
    print("Please generate data set")

tfidf = models.TfidfModel(corpus) # step 1 -- initialize a model

corpus_tfidf = tfidf[corpus] # step 2 -- use the model to transform vectors

lsi = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=2) # initialize an LSI transformation
lsi.print_topics(2)

corpus_lsi = lsi[corpus_tfidf] # create a double wrapper over the original corpus: bow->tfidf->fold-in-lsi

'''
for doc in corpus_lsi: # both bow->tfidf and tfidf->lsi transformations are actually executed here, on the fly
     print(doc)
'''


lsi.save('../tmp/model.lsi') # same for tfidf, lda, ...
