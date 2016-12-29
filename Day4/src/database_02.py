# Database Backup
import sqlite3
from os.path import *

con = sqlite3.connect(':memory:')
cur = con.cursor()
cur.execute("create table PhoneBook (Name text, PhoneNumber text);")
cur.execute("insert into PhoneBook values ('derick', '010-222');")
cur.execute("insert into PhoneBook values ('tom', '010-333');")
cur.execute("insert into PhoneBook values ('dep', '010-444');")
cur.execute("select * from PhoneBook;")
for row in cur:
    print(row)
# SQL 구문으로 출력
dbUrl = realpath('./Day4/src/dump.sql')
with open(dbUrl, "wt") as f:
    for item in con.iterdump():
        f.write("{0}\n".format(item))
