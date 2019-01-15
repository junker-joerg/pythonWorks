# ! git push https://github.com/junker-joerg/pythonworks [jeden Abend]
# ! ... die Automatisierung dazu verstehen
# ! ... Produktion / Entwicklungs-Branch aufziehen
# ! 

"""
Natural Language Processing CIO Tool - 2019 Dr. Martin Köhler

Python Programm zur Auswertung beliebiger (PDF/ PPT) Dateien aus den  Projekten im CIO Umfeld

Analyse der Ergebnisse (eines Corpus) mit Natural Language Processing Werkzeugen mit folgenden Ziele

1. Es wird eine Liste der zu lesenden Dateien-Namen in einem Verzeichnis erstellt
    1.1. Die Dateinamen sollen in die sqlite-Tabelle geschrieben werden
    1.2. Die Unternehemensnamen auch ? aber wo sollen die erkannt werden ?
    1.3. Die SeitenNummer soll auch in die DB rein 
    ? wäre es für interne Weiterverarbeitung besser csv zu schreiben?
    ! Kann später nachgeholt werden
    1.4. Immer die .sqlite3-Datenbank mitführen und committen!
    1.5 Testumgebung: 
        - eine Kopie der Strategie-Docs in ein Verzeichnis
        - eine Kopie des aktuell in Bearbeitung befindlichen Skripts in der gleich Verzeichnis

2. Die Liste wird sequenziell eingelesen und die Texte extrahiert
3. Speicherung der Texte - da die (Raw)texte hinterher mit NLP-Tools wie NLTK / GENSIM weiterverarbeitet
   weiterverarbeitet werden sollen, bietet es sich an, das gleich in den entsprechenden Strukturen von NLTK 
   zu machen

NLTK                            => Einfaches Textcleaning
Einfache Sentimentanalyse       => geht mit NLTK
Topic-Mining                    => hier ggf. GENSIM nutzen
"""

import sys
import locale
import sqlite3

import os
import logging
import logging.handlers as handlers
from PyPDF2 import PdfFileReader
import re
import nltk
import unicodedata


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
"""
?  Globale Variablen ? - zB den Logging-Funktionen? damit diese von 
?  Defs aufgerufen werden können?
"""


def ziel_db_oeffnen():
    # wenn die DB NLP_CIO_TEXT_DB.sqlite3 existiert:
    if os.path.isfile('NLP_CIO_TEXT_DB.sqlite3'):
        if os.path.getsize('NLP_CIO_TEXT_DB.sqlite3') > 100:
            with open('NLP_CIO_TEXT_DB.sqlite3','r', encoding = "ISO-8859-1") as f:
                header = f.read(100)
                if header.startswith('SQLite format 3'):
                    print("NLP_CIO_TEXT_DB.sqlite3 bereits angelegt") # TODO: muss in das Log
    else: # 1) Datenbank anlegen und die Tabellen anlegen - in 
        con = sqlite3.connect('NLP_CIO_TEXT_DB.sqlite3') # ! dann wird sie hier angelegt
        cur = con.cursor() # ! den Cursor auf <oben> setzen
        # TODO: HIER die Tabellen anlegen 
        # Tabelle für Texte aus den geöffneten Dateien anlegen
        tabAnlegen1_sql = """CREATE TABLE texte (id integer PRIMARY KEY, inhalt text NOT NULL)"""
        cur.execute(tabAnlegen1_sql)
        # * Tabelle für die Dateinamen und ggf. die Unternehmensnamen anlegen - done 
        # TODO: diese beiden Felder sind dann aber auch in der Auslesefunktion zu schreiben


def cleaning2(text):
    """
    Funktion aus Stackoverflow - REGEX ist eigenes Thema
        :param text: 
    """
    # ? die Wörter sind nicht zusammengezogen
    #text = re.sub(r'\b(?:(?:https?|ftp)://)?\w[\w-]*(?:\.[\w-]+)+\S*(?<![.,])', ' ', text.lower())
    #words = re.findall(r'[a-z.,]+', text)
    # ! anscheinend muss der ganze Kram re.sub gar nicht sein - 
    # https://regex101.com/ hier testen und einfach! halten - Umlaute erse
    text = text.lower()
    #words = re.findall(r'[a-z.,]+', text)
    words = re.findall(r'\w+', text)
    return ' '.join(words)
 
def text_extractor(path):
    #  ! erst neues Test-Szenario aufbauen - 3 Dateien in einem Verzeichnis 
    with open(path, 'rb') as f: # übergebenen Pfad öffnen
        pdf = PdfFileReader(f) # aus Datei Anzahl Seiten lesen
        pages = pdf.getNumPages() # in Schleifenvariable geben
        num_of_page = 0
        for page in range(pages): # Schleife über Seitenzahl
            num_of_page = num_of_page +  1
            page = pdf.getPage(page)
            text  = page.extractText()
            # print(text)
            text = cleaning2(text)
            
            text_plain = str(text)
            print(text_plain)
            #print(text.encode("utf-8")) # hier muss der RegEx Code rein
            file.write(text_plain)
            #file.write("\n Seite: %i \n" % num_of_page) # Variablenname nicht ähnlich benennen!
            #file.write("\n Dateiname: %s \n" % path)
  
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