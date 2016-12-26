import sqlite3
con = sqlite3.connect(":memory:")
cur = con.cursor()

cur.execute("create table PhoneBook(Name text, Age integer);")
list = (('Tom', 24),('Derick',30),('Peter',53),('Jane',29))
cur.executemany("insert into PhoneBook values(?,?);", list)

cur.execute("select length(name), upper(name), lower(name) from PhoneBook")
print("-- length(), upper(), lower() --")
print([r for r in cur])

cur.execute("select count(*), random(*) from PhoneBook")
print("-- count(*), random(*) --")
print([r for r in cur])
