import sqlite3
con = sqlite3.connect("./commit2.db")
cur = con.cursor()
cur.execute("create table PhoneBook(Name text, PhoneNum text);")
cur.execute("insert into PhoneBook values('derick', '010-111-2222');")
cur.execute("insert into PhoneBook values('Tom', '010-111-2222');")
cur.execute("insert into PhoneBook values('Sangjung', '010-111-2222');")
cur.execute("insert into PhoneBook values('Sam', '010-111-2222');")

con.commit()

