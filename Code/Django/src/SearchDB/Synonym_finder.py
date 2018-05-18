from vocabulary.vocabulary import Vocabulary as vb


def get_syn(x):

    word = x.split()
    syns = []
    for ii in range(0, len(word)):
        s = vb.synonym(word[ii], format='list')
        if s:
            if s[0] not in syns:
                syns.append(s[0])
    return syns
