# -*- coding: UTF-8 -*-
from nltk.corpus import PlaintextCorpusReader
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk import Text
import nltk
import unicodecsv
mytext = "Das ist Satz 1. Satz zwei enthält öüÖÄÜ Umlaute. Satz 3 ist der letzte Satz!"
type(mytext)
tokens = nltk.word_tokenize(mytext, language='german')
print(tokens)
print(type(mytext))
print(type(tokens))
