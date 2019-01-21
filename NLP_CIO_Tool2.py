# Neuer Ansatz mit PDFminer
# http://stanford.edu/~mgorkove/cgi-bin/rpython_tutorials/Using%20Python%20to%20Convert%20PDFs%20to%20Text%20Files.php
# to run: pip install -n mko pdfminer.six
# in Python 3: https://stackoverflow.com/questions/11914472/stringio-in-python3


from io import StringIO # M Köhler: wegen Python 3 
import numpy
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
import os
import sys, getopt
from nltk.corpus import PlaintextCorpusReader
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk import Text

#converts pdf, returns its text content as a string
def convert(fname, pages=None):
    if not pages:
        pagenums = set()
    else:
        pagenums = set(pages)

    output = StringIO()
    #output =  numpy.genfromtxt(io.BytesIO(encode())) # wegen Python3
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

def convertMultiple(pdfDir, txtDir):
    if pdfDir == "": pdfDir = os.getcwd() + "\\" #if no pdfDir passed in ? heisst das, dass er in C:/ sucht?
    for pdf in os.listdir(pdfDir): #iterate through pdfs in pdf directory
        fileExtension = pdf.split(".")[-1]
        if fileExtension == "pdf":
            pdfFilename = pdfDir + pdf 
            text = convert(pdfFilename) #get string of text content of pdf
            # 
            textFilename = txtDir + pdf + ".txt"
            #textFile = open(textFilename, "w", encoding="utf-8", errors="ignore") #make text file
            textFile = open(textFilename, "w", encoding="utf-8", errors="replace") # ascii geht durch - aber Umlaute weg
            #textFile = open(textFilename, "w", encoding="cp1252", errors="replace") # ascii geht durch - aber Umlaute weg
            
            textFile.write(text) #write text to text file
            # hier nun in den Corpus schreiben
            # https://stackoverflow.com/questions/4951751/creating-a-new-corpus-with-nltk
            newcorpus = PlaintextCorpusReader("C:/Users/mkoehler1/Documents/Python Scripts/pythonworks/", ".*.txt")
            # https://stackoverflow.com/questions/9149709/extracting-words-using-nltk-from-german-text
            # nltk.Text nimmt KEIN Unicode ... Danke, Python3!
            # coded = [ tok.encode('utf-8') for tok in newcorpus.words(textFile) ]
            # zielcorpus = nltk.Text(coded)
            zielcorpus  = Text(newcorpus.words())
            #print(newcorpus.raw().strip())
            #saetze = sent_tokenize(zielcorpus)
            print(newcorpus.sents()) # im Moment scheinen die Sätze nicht abgegrenzt zu sein
            print(newcorpus.words())
            print(newcorpus.paras)
            print(newcorpus.CorpusView.fileid)
            
if __name__ == "__main__":
    pdfDir = "C:/Users/mkoehler1/Documents/Python Scripts/pythonworks/"
    txtDir = "C:/Users/mkoehler1/Documents/Python Scripts/pythonworks/" # aktuelles VZ ? unklar
    convertMultiple(pdfDir, txtDir)
     # nltk.data.path.append(b"C:\Users\mkoehler1\AppData\Roaming\nltk_data")