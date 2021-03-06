import logging
from gensim import corpora
from stop_words import get_stop_words
from collections import defaultdict
from pprint import pprint  # pretty-printer
from six import iteritems
import codecs
import re
import os
import sys


def file_read(filename):
    # using utf-8 might have problem
    file = codecs.open(filename, 'r', 'utf-8')
    content = file.read()
    return content

# logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO) # see logging events


def vector_space_convert(ArticlePath, DictPath, mmPath, filename):
    '''
    # test filename
    filename = ['../../papers/Cobelli1979_Identifiability_of_compartmental_systems_and_related_structural_properties.txt',
                '../../papers/Li2012_Development_Of_Multi-fingered_Robotic_Hand.txt',
                '../../papers/Miao2011_On_identifiability_of_nonlinear_ODE_models_and_applications_in_viral_dynamics.txt',
                '../../papers/Vajad1989_Similarity_transformation_approach_to_identifiability_a_alysis_of_nonlinear_compartmental_models.txt',
                '../../papers/Villaverde2016_Structural_Identifiability_of_Dynamic_Systems_Biology_Models.txt']


    # read file
    for count in range(0, 5):
        documents.append(file_read(filename[count]))
    '''
    documents = []  # list for storing documents

    # count = 0

    for articles in os.listdir(ArticlePath):
        # print file_read(tmp)
        # print "count = %d" % count
        # count += 1
        documents.append(file_read(ArticlePath + articles))

    # print documents[37]
    # print "okay"

    # remove common words and tokenize
    stop_words = get_stop_words('english')  # getting english stop_words
    texts = [[word for word in document.lower().split() if word not in stop_words]
             for document in documents]

    # remove words that appear only once
    frequency = defaultdict(int)
    for text in texts:
        for token in text:
            frequency[token] += 1
    texts = [[token for token in text if frequency[token] > 1]
             for text in texts]

    # regular expression removing non-alphabet character
    texts = [[re.sub('[^A-Za-z]', '', token) for token in text]
             for text in texts]
    texts = [filter(None, text)
             for text in texts]  # remove empty entry of a list

    dictionary = corpora.Dictionary(texts)
    once_ids = [tokenid for tokenid, docfreq in iteritems(
        dictionary.dfs) if docfreq == 1]
    # remove stop words and words that appear only once
    dictionary.filter_tokens(once_ids)
    dictionary.compactify()  # remove gaps in id sequence after words that were removed

    '''
    for i in range(0, 9999):
        print dictionary[i]
    '''

    # store the dictionary, for future reference
    dictionary.save(DictPath + filename + '.dict')

    corpus = [dictionary.doc2bow(text) for text in texts]
    # store to disk, for later use
    corpora.MmCorpus.serialize(mmPath + filename + '.mm', corpus)
