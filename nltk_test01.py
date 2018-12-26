# https://stackoverflow.com/questions/9149709/extracting-words-using-nltk-from-german-text
# 26.12.2018

import os
import nltk
import random
import re, pprint
from nltk import word_tokenize
from nltk.corpus import gutenberg

deutsch ="Dieses Unterfangen wird nicht von Erfolg gekrönt sein"

