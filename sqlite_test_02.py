# https://stackabuse.com/a-sqlite-tutorial-with-python/ 
# Nicht aus Workflow starten, da sqlite dann versucht, das db.file auf git anzulegen
# falls nur im pythonista-Verzeichnis anlegbar: schade - aber ist dann so
# eine sqlitemaster.db anlegen - da kommt dann alles rein
# zb
# os.listdir('/private/var/mobile/Library/Mobile Documents/iCloud~com~omz-software~Pythonista3/Documents') 

import sqlite3
import os

def openDB():
	con = sqlite3.connect("MkDev.db")


def sqliteCMDs(): # Global - Lokal - Problem?
	global lisqlcmd
	lisqlcmd = [
		"CREATE TABLE VUtab (id integer PRIMARY KEY, VUname text NOT NULL, Bemerkung text NOT NULL)", #0
		"CREATE TABLE SHUKpi (id integer PRIMARY KEY, GWP real NULL, Claims float, Bemerkung text NULL)",
		"CREATE TABLE SUmarkt (id integer PRIMARY KEY, transAc integer, FOREIGN KEY (SHUKpi_id) REFERENCES SHUKpi (id))"
		# hier dann die INPUT-Befehle einbauen
		"insert into VUname(VUname, Bemerkung) values (?, ?), VN, VNremark)"
		# hier die select-Befehle
		"select firstname, lastname from person" 
	]

if __name__ == "__main__":
	openDB()
	sqliteCMDs()
	print(lisqlcmd[1])
	#sql-lite speichern
