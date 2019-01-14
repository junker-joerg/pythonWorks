"""
Dokumentation nachziehen!!!   
"""
import os
import logging
import logging.handlers as handlers
from PyPDF2 import PdfFileReader
import re
# TODO: alles Statusinfos in Logfile schreiben
# TODO: dafür Modul Logger nutzen
"""
clean_up_a(textinput): möglichst allen Müll raus
https://codereview.stackexchange.com/questions/186614/text-cleaning-script-producing-lowercase-words-with-minimal-punctuation
"""

def cleaning2(text):
    # ? die Wörter sind nicht zusammengezogen
    text = re.sub(r'\b(?:(?:https?|ftp)://)?\w[\w-]*(?:\.[\w-]+)+\S*(?<![.,])', ' ', text.lower())
    words = re.findall(r'[a-z.,]+', text)
    return ' '.join(words)
 
def text_extractor(path):
    with open(path, 'rb') as f: # übergebenen Pfad öffnen
        pdf = PdfFileReader(f) # aus Datei Anzahl Seiten lesen
        pages = pdf.getNumPages() # in Schleifenvariable geben
        num_of_page = 0
        for page in range(pages): # Schleife über Seitenzahl
            num_of_page = num_of_page +  1
            page = pdf.getPage(page)
            #print(page) # nur drucken - hier in DB speichern
            #print('Page type: {}'.format(str(type(page))))
            text = page.extractText()
            text = cleaning2(text)
            text_plain = str(text)
            #print(text.encode("utf-8")) # hier muss der RegEx Code rein
            file.write(text_plain)
            file.write("\n Seite: %i \n" % num_of_page) # Variablenname nicht ähnlich benennen!
            file.write("\n Dateiname: %s \n" % path)
  
    # decoding-Problem! ... neu lernen!! - wie wird aus dem Output ein String?

if __name__ == '__main__': # liste aller PDF im Verzeichnis
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')	
    logHandler = logging.FileHandler('FS_DB_strategy_NLP.log', mode="a")
    logHandler.setFormatter(formatter)
    logger.addHandler(logHandler)
    logger.info("Starte Logging")

    files = [x for x in os.listdir() if x.endswith(".pdf")]
   # print(files)
    logger.info("Starte Logging")   
    file = open("pdf_txt.txt","w") # Ergebnis einfach in Datei
    logger.info("Zieldatei geöffnet")
    for eachfile in files:
        #path = eachfile
        #print(eachfile)
        logger.info("Quelldatei %s geöffnet" %eachfile)
        text_extractor(eachfile) # ... damit Unterfunktion aufrufen
    file.close()