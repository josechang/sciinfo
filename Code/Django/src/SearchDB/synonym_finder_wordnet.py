#pip install -U nltk
#nltk.download('wordnet')
import nltk
from nltk.corpus import wordnet as wn

def get_syn(x):
	word    = x.split()	# Spilt the input sentence to seperate words
	suggest = []		# Suggestion for each words
	syns    = []		# Final output
	
	for ii in range(0, len(word)):
		
		if not wn.synsets(word[ii]): # Check if it's empty
			syns.append('False')
		else:
			sets = wn.synsets(word[ii])[0].lemma_names()
			
			if len(sets)<2:
				suggest = False
			else:
				if sets[0] != word[ii]:	 # Check if the first word equals to the input
					suggest = sets[0]
				else:
					suggest = sets[1]
				
		syns.append(suggest)
			
	return syns
				

#q = get_syn('artificial_intelligence feedback')			
#print(q, wn.synsets('feedback')[0].lemma_names())
#syns = wn.synsets('artificial_intelligence')[0].hypernyms()[0].lemma_names()
