import sqlite3
from Main import to_day, Journal_Entry

DB = sqlite3.connect("Journals.sqlite")
iterator = DB.cursor()

iterator.execute("create table Journals (Journal_Entry, to_day)")
iterator.execute("Insert into Journals values ('Good', 7/26/2018)")

print("Database")

for Journal_Entry in iterator.fetchall():
        print(Journal_Entry)
