# -*- coding: utf-8 -*-
# ! git push https://github.com/junker-joerg/pythonworks [jeden Abend]
# ! Das Beste aus den Vorversionen NLP_CIO_Tool2.py,  NLP_CIO_Tool.py...
# ! ... corpusclean.py und CorpUniC01.py übernehmen
# ToDO: über alle Dateien - aus jeder Datei wird mit PDFminer der Text gezogen und ín eine neue Datei kopiert   
# ToDO: in einem zweiten Schritt werden die .txt-Dateien durch die Cleaner-Funktionen geschickt und dann wird
# ToDO: die REIN-Datei für den Corpus geschrieben - es wird im LogFile vermerkt, wieviel Sätze / Worte geschrieben
# ToDO: wurden
# ------------------------------------ IMPORT Sektion ---------------------------------------------
from nltk.corpus import PlaintextCorpusReader
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk import Text
import nltk
import unicodecsv
from io import StringIO # M Köhler: wegen Python 3 
import numpy
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import os
import sys, getopt
import re
import logging
import logging.handlers as handlers
# ------------------------------------ IMPORT Sektion ---------------------------------------------

#converts pdf, returns its text content as a string
def convert(fname, pages=None):
    if not pages:
        pagenums = set()
    else:
        pagenums = set(pages)

    output = StringIO()
    manager = PDFResourceManager()
    converter = TextConverter(manager, output, laparams=LAParams())
    interpreter = PDFPageInterpreter(manager, converter)

    infile = open(fname, 'rb')
    for page in PDFPage.get_pages(infile, pagenums):
        interpreter.process_page(page)
    infile.close()
    converter.close()
    text = output.getvalue() # ... wenn man was rausfiltern will: dann auch hier
    output.close
    return text 

def txtclean(text):
    re.sub(' +', ' ',text) # http://www.datasciencemadesimple.com/remove-spaces-in-python/
    re.sub('- ', '',text)
    re.sub(' -', '',text)
    tokens = nltk.word_tokenize(text, language='german') # ? ist das hier richtig vom Ablauf?
    i = 0
    for i in range(len(tokens)):
        recode = str(tokens[i]).encode().decode("UTF-8") # das funktioniert! ... entspricht aber nicht dem Video?!
        # print(recode) # ! hier überflüssig, da Textdatei in <convertMultiple> geschrieben wird
        i = i + 1
    logger.info("Anzahl Tokens geschrieben %i " %len(tokens))
    return text # ! oder recode? 

def convertMultiple(pdfDir, txtDir):
    if pdfDir == "": pdfDir = os.getcwd() + "\\" #if no pdfDir passed in  
    for pdf in os.listdir(pdfDir): #iterate through pdfs in pdf directory
        fileExtension = pdf.split(".")[-1]
        if fileExtension == "pdf":
            pdfFilename = pdfDir + pdf 
            text = convert(pdfFilename) #get string of text content of pdf
            txtclean(text) # ! hier den Aufruf der eigenen Textclearingfunktion
            textFilename = txtDir + pdf + ".txt"
            textFile = open(textFilename, "w", encoding="utf-8", errors="replace") # ascii geht durch - aber Umlaute weg
            textFile.write(text) #write text to text file
            logger.info("Zieldatei %s geschrieben" %textFilename) # ! Logger
            #zielcorpus  = Text(newcorpus.words())
            

# ! Main & Logging
if __name__ == "__main__":
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')	
    logHandler = logging.FileHandler('NLP_CIO_Tool.log', mode="a")
    logHandler.setFormatter(formatter)
    logger.addHandler(logHandler)
    logger.info("Starte Logging")

    pdfDir = "C:/Users/MKoehler1/Documents/Python Scripts/itstratcorpus/"
    txtDir = "C:/Users/MKoehler1/Documents/Python Scripts/itstratcorpus/" # aktuelles VZ ? unklar
    
    convertMultiple(pdfDir, txtDir)
     # nltk.data.path.append(b"C:\Users\mkoehler1\AppData\Roaming\nltk_data") # ! wenn der deutsche Tokenizer PUNKT nicht gefunden wird 
        
    # ? hier die Corpusverarbeitung aufrufen?
 

    newcorpus = PlaintextCorpusReader(txtDir, ".*.txt") # ? hier corpus aufbauen
    #! tokens = nltk.word_tokenize(worte, language='german') wird durch den PlaintextCorpusReader sowieso aufgerufen
    # ! print(newcorpus.paras(newcorpus.fileids()[0])) Logger 
    
    logger.info("Anzahl Worte im Corpus %i " %len(newcorpus.words()))
    logger.info("Anzahl Sätzt im Corpus %i " %len(newcorpus.sents()))
    logger.info("Anzahl Paragraphen im Corpus %i " %len(newcorpus.paras()))
    
    