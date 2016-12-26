import sqlite3
con = sqlite3.connect(":memory:")
cur = con.cursor()
cur.execute("create table PhoneBook(Name text, PhoneNum text);")
cur.execute("insert into PhoneBook Values('Derick', '010-1234-5678');")
cur.execute("insert into PhoneBook Values('bb', '010-1234-5678');")
cur.execute("insert into PhoneBook Values('cc', '010-1234-5678');")
cur.execute("insert into PhoneBook Values('dd', '010-1234-5678');")


cur.execute("select * from PhoneBook;")
for row in cur:
    print(row)
    
