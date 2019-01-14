
# ! git push https://github.com/junker-joerg/pythonworks [jeden Abend]
# ! ... die Automatisierung dazu verstehen
# ! ... Produktion / Entwicklungs-Branch aufziehen

"""
Natural Language Processing CIO Tool - 2019 Dr. Martin Köhler

Python Programm zur Auswertung beliebiger (PDF/ PPT) Dateien aus den  Projekten im CIO Umfeld

Analyse der Ergebnisse (eines Corpus) mit Natural Language Processing Werkzeugen mit folgenden Ziele

1. Es wird eine Liste der zu lesenden Dateien-Namen in einem Verzeichnis erstellt
2. Die Liste wird sequenziell eingelesen und die Texte extrahiert
3. 

NLTK                            => Einfaches Textcleaning
Einfache Sentimentanalyse       => geht mit NLTK
Topic-Mining                    => hier ggf. GENSIM nutzen
"""
import os
import logging
import logging.handlers as handlers
from PyPDF2 import PdfFileReader
import re
# TODO: alles Statusinfos in Logfile schreiben
# TODO: dafür Modul Logger nutzen
# * Wichtig CLIPS.patterns ausprobieren - ggf. kann das schneller gehen
# ! Achtung bislang wird NLTK auch noch nicht geladen
# TODO: TEST es gibt keinerlei Textfunktionen 
# TODO: https://adfinis-sygroup.ch/blog/testing-mit-pytest/
# 
"""
clean_up_a(textinput): möglichst allen Müll raus
https://codereview.stackexchange.com/questions/186614/text-cleaning-script-producing-lowercase-words-with-minimal-punctuation
"""

def cleaning2(text):
    """
    Funktion aus Stackoverflow - REGEX ist eigenes Thema
        :param text: 
    """
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
    # ! Den Logger im Zweifel in <main> starten - aber ggf. kann man das auch in eine Funktion auslagern
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')	
    logHandler = logging.FileHandler('NLP_CIO_Tool.log', mode="a")
    logHandler.setFormatter(formatter)
    logger.addHandler(logHandler)
    logger.info("Starte Logging")

    files = [x for x in os.listdir() if x.endswith(".pdf")] # ! bislang wird hier noch eine Liste der PDFs generiert - PPT ist noch offen
    # TODO: Klären, was das bessere Zielformat ist und das optimale Speicherformat a) sqlite, b) .txt c) csc (tabbed)
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