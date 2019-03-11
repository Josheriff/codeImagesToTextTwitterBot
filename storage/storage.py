import sqlite3
conn = sqlite3.connect('my_database.sqlite')
cursor = conn.cursor()
print("Opened database successfully")