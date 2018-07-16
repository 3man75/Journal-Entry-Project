import sqlite3
from Main import to_day, Journal_Entry

conn = sqlite3.connect('Story_Journals.db')

cursor = conn.cursor()

def create_table():
    cursor.execute('THis will be a table. (datestamp TEXT, )')

def data_entry():
    cursor.execute("""INSERT DATA FOR JOURNALS:""")
    conn.commit()
    conn.close()
    print(to_day,Journal_Entry)


conn.close()
conn.commit()



#create_table()
#data_entry()
