# -*- coding: utf-8 -*-
# corpus cleaner git push https://github.com/junker-joerg/pythonworks
import os
import re
import nltk
from nltk import word_tokenize

mytext = open ("BHW_IT-Strategie.pdf.txt", "r") # den Text neu schreiben lassen - als ISO oder cp1252
worte = mytext.read()
re.sub(' +', ' ',worte) # http://www.datasciencemadesimple.com/remove-spaces-in-python/
re.sub('- ', '',worte)
re.sub(' -', '',worte)
tokens = nltk.word_tokenize(worte, language='german')
#print(tokens) # ohne Umlaute als Unicode UTF-8
i = 0
for i in range(len(tokens)):
    recode = str(tokens[i]).encode().decode("UTF-8") # das funktioniert! ... entspricht aber nicht dem Video?!
    print(recode)
    i = i + 1
print("Token: ")
print(len(tokens))