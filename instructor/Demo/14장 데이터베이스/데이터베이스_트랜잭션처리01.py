import sqlite3
con = sqlite3.connect("./test.db")
cur = con.cursor()
cur.execute("create table PhoneBook(Name text, PhoneNum text);")
cur.execute("insert into PhoneBook values('derick', '010-111-2222');")
cur.execute("select * from PhoneBook;")
print(cur.fetchall())
