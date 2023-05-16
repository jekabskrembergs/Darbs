import sqlite3

conn = sqlite3.connect("datasheeet.db")
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS persons (id INTEGER PRIMARY KEY, name VARCHAR, surname VARCHAR)")

conn.commit()

name = input("vards: ")
surname = input("uzvards: ")

cursor.execute("INSERT INTO persons (name, surname) VALUES (?, ?)", (name, surname))
conn.commit()

identif = int(input("delete id: "))
cursor.execute("DELETE FROM persons WHERE id = ?", str(identif))
conn.commit()



