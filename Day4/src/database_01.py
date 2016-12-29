import sqlite3
from os.path import *

dbUrl = realpath('./Day4/src/commit.db')
con = sqlite3.connect(dbUrl)
cur = con.cursor()
cur.execute("create table PhoneBook (Name text, PhoneNumber text);")
cur.execute("insert into PhoneBook values ('derick', '010-222');")
cur.execute("select * from PhoneBook;")
for row in cur:
    print(row)
con.commit()
con.close()