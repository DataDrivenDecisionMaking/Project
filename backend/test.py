import sqlite3

conn = sqlite3.connect('/Users/manishsingh/SEM4/downloads/sqlite-autoconf-3120100/team1DB.db')

print conn

print "Opened database successfully"

cursor = conn.execute("SELECT name from test")

for row in cursor:
	print "Name:=", row[0]

print "Operation done successfully";

conn.close()

