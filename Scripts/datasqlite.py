import sqlite3

conn = sqlite3.connect('db.sqlite3.db')
c = conn.cursor()
print("Opened database successfully")

cursor = c.execute("SELECT id from ")