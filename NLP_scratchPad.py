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


if __name__ == "__main__":
    # TODO: https://adfinis-sygroup.ch/blog/testing-mit-pytest/ für Testing
    # ziel_db_oeffnen() # läuft!
    #schreibe_Texte_in_Tabelle()
    #print(remove_accented_chars("gesch�ftsstrategie  ke zur verf�gung "))
    #print(text_to_id("gesch�ftsstrategie  ke zur verf�gung "))
    print(mkReTest((u"Änderung")))
    print("ENDE")
