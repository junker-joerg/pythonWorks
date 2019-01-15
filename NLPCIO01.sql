/*  kleines SQLite-Skript, um die Tabellen in NLP_CIO_TEXT_DB.sqlite3 anzulegen
 *  Ur-Version: 15.01.2019
 *  Martin Köhler
 *  Ausfürhung: 
 *  sqlite3  
 * .read NLPCIO01.sql
 */

CREATE TABLE dateinamen (id integer PRIMARY KEY, dateiname text NOT NULL)