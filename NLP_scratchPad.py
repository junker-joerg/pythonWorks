#!python
# ! git push https://github.com/junker-joerg/pythonworks
# ! Die Testfunktion einfach runterschreiben - dann in eine Funktion <def> reinkopieren
# oder besser: Test in eine Funktion schreiben und in Main reinkopieren

import os
import sys
import sqlite3

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



if __name__ == "__main__":
    # TODO: https://adfinis-sygroup.ch/blog/testing-mit-pytest/ für Testing
    # ziel_db_oeffnen() * läuft!
    print("ENDE")
