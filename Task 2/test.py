import os
import json
from nltk import PorterStemmer, WordNetLemmatizer, pos_tag

text = """Welcome you to programming knowledge. Lets start with our first tutorial on NLTK. We shell learn bascis of NLTK here."""
demoWords = ['playing', 'happiness', 'going', 'doing', 'yes', 'no', 'I', 'having', 'had', 'haved', 'coding', 'programming', 'code', 'program', 'playing']

lematizer = WordNetLemmatizer()
ps = PorterStemmer()

lemaList = ['a', 's', 'r', 'n', 'v']

print([i for i in lemaList])

# for word in demoWords:
    # Left side is the stemmer and the right side is lemmatizer.
    # print(word, ps.stem(word), lematizer.lemmatize(word, pos=))