# ! git push https://github.com/junker-joerg/pythonworks
# ! Die Testfunktion einfach runterschreiben - dann in eine Funktion <def> reinkopieren
# oder besser: Test in eine Funktion schreiben und in Main reinkopieren

import sqlite3

def ziel_db_oeffnen():
    try:
        # ! https://stackoverflow.com/questions/12932607/how-to-check-if-a-sqlite3-database-exists-in-python
        
        DEFAULT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))    
        con = sqlite3.connect('NLP_CIO_db.sqlite3') # gibt es die DB schon?
    else:
        pass
    pass

def ziel_tabellen_anlegen():
    try:
        pass
    except expression as identifier:
        pass
    else:
        pass

if __name__ == "__main__":
    # TODO: https://adfinis-sygroup.ch/blog/testing-mit-pytest/ für Testing
    pass