# sqlite DB anlegen
# https://stackabuse.com/a-sqlite-tutorial-with-python/
# git remote add upstream https://github.com/junker-joerg/pythonWorks
# git push -u origin master
# ... irgendwas ...noch was 
# git remote add origin 'https://github.com/junker-joerg/pythonWorks'
#... hier ein neuer Kommentar
# neuer Kommentar auf PC Wohnzimmer geschrieben

import sqlite3
import os

con = sqlite3.connect('mkDevDB.sqlite3') 
DEFAULT_PATH = os.path.join(os.path.dirname(__file__), 'database.sqlite3')

def db_connect(db_path=DEFAULT_PATH):  
    con = sqlite3.connect(db_path)
    return con

con = db_connect('mkDevDB.sqlite3') # connect to the database
cur = con.cursor() # instantiate a cursor obj



#products_sql = """CREATE TABLE products (id integer PRIMARY KEY, name text NOT NULL, price real NOT NULL)"""
#cur.execute(products_sql)


product_sql = "INSERT INTO products (name, price) VALUES (?, ?)"
cur.execute(product_sql, ('Introduction to Combinatorics', 7.99))
cur.execute(product_sql, ('A Guide to Writing Short Stories', 17.99))
cur.execute(product_sql, ('Data Structures and Algorithms', 11.99))
cur.execute(product_sql, ('Advanced Set Theory', 16.99))