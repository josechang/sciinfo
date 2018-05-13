#pip install -U nltk
#nltk.download('wordnet')
import nltk
from nltk.corpus import wordnet as wn

def get_syn(x):

	word = x.split()
	syns = []
	for ii in range(0, len(word)):
		
		if not wn.synsets(word[ii]): # check if it's empty
			syns.append('False')
		else:
			sets = wn.synsets(word[ii])[0].lemma_names()
			syns.append(sets)
			
			"""
			if not sets.hypernyms():
				syns.append('False')
			else:
				syns.append(sets.hypernyms()[0].lemma_names()[0:5])
			"""
	return syns
				

q = get_syn('machine_learning deep_learning neural_network')			
print(q)
#syns = wn.synsets('artificial_intelligence')[0].hypernyms()[0].lemma_names()