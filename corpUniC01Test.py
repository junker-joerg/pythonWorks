# -*- coding: utf-8 -*-
from nltk.corpus import PlaintextCorpusReader
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk import Text
import nltk
#import unicodecsv
mytext = u"Das ist Satz 1. Satz zwei enthält öüÖÄÜ Umlaute. Satz 3 ist der letzte Satz!"
type(mytext)
tokens = nltk.word_tokenize(mytext, language='german')
print(tokens) # ohne Umlaute als Unicode UTF-8
i = 0
for i in range(len(tokens)):
    recode = str(tokens[i]).encode().decode("CP1252") # das funktioniert! ... entspricht aber nicht dem Video?!
    print(recode)
    i = i + 1
