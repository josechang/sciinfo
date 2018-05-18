# pip install -U nltk
nltk.download('wordnet')
import nltk
from nltk.corpus import wordnet as wn
from random import randint


def get_syn(x):
    word = x.split()  # Spilt the input sentence to seperate words
    suggest = []		# Suggestion for each words
    syns = []		# Final output
    for ii in range(0, len(word)):

        if not wn.synsets(word[ii]):  # Check if it's empty
            syns.append('False')
        else:
            all_syns = []
            for syn in wn.synsets(word[ii]):
                for l in syn.lemmas():
                    if l.name() != word[ii]:
                        all_syns.append(l.name())

            id = randint(0, len(all_syns)-1)
            suggest = all_syns[id]

            syns.append(suggest)

    return syns  # , all_syns


#syns, all_syns = get_syn('artificial_intelligence  help help machine')
# print(syns)
# print(all_syns)
#syns = wn.synsets('artificial_intelligence ')[0].lemmas()[0].name()
