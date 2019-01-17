#!python
# -*- coding: utf-8 -*-
# ! git push https://github.com/junker-joerg/pythonworks
# ! Die Testfunktion einfach runterschreiben - dann in eine Funktion <def> reinkopieren
# oder besser: Test in eine Funktion schreiben und in Main reinkopieren

import os
import sys
import sqlite3
import unicodedata
import re
import codecs


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
        tabAnlegen1_sql = """CREATE TABLE texte (id integer PRIMARY KEY, inhalt text NOT NULL)"""
        cur.execute(tabAnlegen1_sql)

def schreibe_Texte_in_Tabelle():
    # sqlite insert-Funktion mit parameter-übergabe
    # product_sql = "INSERT INTO products (name, price) VALUES (?, ?)"
    # cur.execute(product_sql, ('Introduction to Combinatorics', 7.99))
    # cur.execute("insert into contacts (name, phone, email) values (?, ?, ?)", (name, phone, email))
    # cur.executemany("insert into contacts (name, phone, email) values (?, ?, ?)", (name, phone, email))
    # https://stackoverflow.com/questions/44678695/how-to-insert-variable-to-database-table-sqlite3-python
    """
    def insertData(self):
        title_Data = self.edit_title.text()
        year_Data = self.edit_year.text()
        rating_Data = self.edit_rating.text()


        connection = sqlite3.connect('films.db')
        try:
            connection.execute("INSERT INTO FILMS (TITLE,YEAR,RATING) VALUES(title_Data,year_Data,rating_Data)")


        except sqlite3.IntegrityError:
            print("You have already stored this data")
        connection.commit() # ! nicht vergessen!
        connection.close()
    """
    # Testdaten generieren und in einer Schleife ausgehen - sql-insert-strings generieren und in NLP_CIO_TEXT_DB.sqlite3 schreiben
    # hier dann die DB öffnen
    con = sqlite3.connect('NLP_CIO_TEXT_DB.sqlite3')
    cur = con.cursor()  
    for i in range (20):
        dN = "Dateiname"+str(i) 
        print(i, dN)
        cur.execute("insert into dateinamen (id, dateiname) values (?, ?)", (i, dN))
    con.commit()
    con.close()


def remove_accented_chars(text):
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8', 'ignore')
    return text

def strip_accents(text):
    """
    Strip accents from input String.

    :param text: The input string.
    :type text: String.

    :returns: The processed String.
    :rtype: String.
    """
    try:
        text = unicode(text, 'utf-8')
    except (TypeError, NameError): # unicode is a default on python 3 
        pass
    text = unicodedata.normalize('NFD', text)
    text = text.encode('ascii', 'ignore')
    text = text.decode("utf-8")
    return str(text)

def text_to_id(text):
    """
    Convert input text to id.

    :param text: The input string.
    :type text: String.

    :returns: The processed String.
    :rtype: String.
    """
    text = strip_accents(text.lower())
    text = re.sub('[ ]+', '_', text)
    text = re.sub('[^0-9a-zA-Z_-]', '', text)
    return text

def mkReTest(text): #  alle Umlaute ersetzen
    text = re.compile('[^a-zA-Z0-9]')
    text.subn('_', text)
    return text

def roheinlesen(): # Einlesen der Ergebnis-Datei des Auslesens aus der / den PDF-Dateien
    with codecs.open("pdf_txt.txt", "r", encoding="UTF-16 LE", errors="ignore") as f:
        i = 0
        for line in f:
            #l = str(line.encode(encoding="utf-8", errors="ignore"))
            l = str(re.sub(r'[^\x00-\x7f,\xF6,\xE4]',r'', line)) # Umlaute drin lassen! ... fehlen aber noch
            #l = str(re.sub(r'[^\x00-\x7f',r'', line)) 
            #l = str(re.sub(r'[^\x00-\x7f]',r'', line)) 
            #l = " ".join(re.split("\s+", l, flags=re.UNICODE))
            #l = " ".join(line.split())
            print(l)
            i = i +1
        print(i)
        
    #	data = f.read().decode("utf8").encode("ascii", errors="ignore").decode()

    #tokens = word_tokenize(data)

# Small example hot to convert german special characters from unicode to utf-8 and back to unicode
# http://www.utf8-zeichentabelle.de/unicode-utf8-table.pl?start=128&number=128&names=-&utf8=string-literal
#

umlaute_dict = {
    '\xc3\xa4': 'ae',  # U+00E4	   \xc3\xa4
    '\xc3\xb6': 'oe',  # U+00F6	   \xc3\xb6
    '\xc3\xbc': 'ue',  # U+00FC	   \xc3\xbc
    '\xc3\x84': 'Ae',  # U+00C4	   \xc3\x84
    '\xc3\x96': 'Oe',  # U+00D6	   \xc3\x96
    '\xc3\x9c': 'Ue',  # U+00DC	   \xc3\x9c
    '\xc3\x9f': 'ss',  # U+00DF	   \xc3\x9f
}

def cleaning2(unicode_string):
    """
    # ! ACHTUNG: der pdf-reader generiert eine UTF-16 LE Codierung - siehe scratch-Pad 
    # ? die Wörter sind nicht zusammengezogen
    #text = re.sub(r'\b(?:(?:https?|ftp)://)?\w[\w-]*(?:\.[\w-]+)+\S*(?<![.,])', ' ', text.lower())
    #words = re.findall(r'[a-z.,]+', text)
    # ! anscheinend muss der ganze Kram re.sub gar nicht sein - 
    # https://regex101.com/ hier testen und einfach! halten
    umlautDictionary = {u'Ä': 'Ae',
                    u'Ö': 'Oe',
                    u'Ü': 'Ue',
                    u'ä': 'ae',
                    u'ö': 'oe',
                    u'ü': 'ue'
                    }
    
    text = text.lower()
    words = (re.findall(r'[a-z.,]+', text))
    #words = re.findall(r'\w+', text)
    return (' '.join(words))
    """
    utf8_string = unicode_string.encode('utf-8')
    for k in umlaute_dict.keys():
        utf8_string = utf8_string.replace(k, umlaute_dict[k])
    return utf8_string.decode()

def replace_german_umlaute(unicode_string):

    utf8_string = unicode_string.encode('utf-8')

    for k in umlaute_dict.keys():
        utf8_string = utf8_string.replace(k, umlaute_dict[k])

    return utf8_string.decode()

def nltkCorpusReadMK():
    # nltk.data.path.append(b"C:\Users\mkoehler1\AppData\Roaming\nltk_data") # als absoluter Pfad _NICHT_ portabel
    # ! Lese die Datei pdf_txt.txt mit ("pdf_txt.txt", "r", encoding="UTF-16 LE", errors="ignore") als 
    # ! Plain Text Dokument ein
    # ! führe einfache NLTK-Operationen wie tokenize durch
    # ! Small Prof-of-Concept
    from nltk.corpus import PlaintextCorpusReader
    newcorpus = PlaintextCorpusReader("/.", 'pdf_txt.txt') # ... entweder eine Datei oder mehrere
    newcorpus.words('my_corpus.txt')
    newcorpus.words('pdf_txt.txt')
    # ! UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff in position 0: invalid start byte


def UmlauteMK(text):
    mapping = {ord(u"ü"): u"ue", ord(u"ß"): u"ss"}
    return(str(text.translate(mapping)))
    # hier geht es nicht, aber hier geht es!
    # https://www.python-forum.de/viewtopic.php?t=15177



if __name__ == "__main__":
    # TODO: https://adfinis-sygroup.ch/blog/testing-mit-pytest/ für Testing
    # ziel_db_oeffnen() # läuft!
    #schreibe_Texte_in_Tabelle()
    #print(remove_accented_chars("gesch�ftsstrategie  ke zur verf�gung "))
    #print(text_to_id("gesch�ftsstrategie  ke zur verf�gung "))
    #print(mkReTest((u"Änderung")))
    roheinlesen()
    #nltkCorpusReadMK()
    #print(decodeMK("Änderunääüü")) # Anderunaauu
    #print(decodeMK("gesch�ftsstrategie  ke zur verf�gung "))
print("ENDE")
