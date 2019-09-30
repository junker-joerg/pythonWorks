/*  kleines SQLite-Skript, um die Tabellen in NLP_CIO_TEXT_DB.sqlite3 anzulegen
 *  Ur-Version: 15.01.2019
 *  Martin Köhler
 *  Ausführung: 
 *  sqlite3  
 * .read NLPCIO01.sql
 * sqlite3 NLP_CIO_TEXT_DB.sqlite3 'SELECT * FROM dateinamen;'
 * geht auch
 * ToDos: Datenstruktur durchaus mit SQLite Studio erweitern und auch testen - u.a. sqlite3.import 
 */

CREATE TABLE dateinamen (id integer PRIMARY KEY, dateiname text NOT NULL)