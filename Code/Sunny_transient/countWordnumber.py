from sys import argv

script, filename = argv


num_words = 0
 
with open(filename, 'r+') as f:
    for line in f:
        words = line.split()
        num_words += len(words)
    f.write('\n# of words: '+str(num_words))
    print f.read()
    f.close()
#print"Number of words: %r" %num_words

