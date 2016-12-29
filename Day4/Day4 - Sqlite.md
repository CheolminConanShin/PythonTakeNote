### SQLite3
임시 메모리에 DB 생성
```python
import sqlite3
con sqlite3.connect(':memory') # Temporary Database
cur = con.cursor()
cur.execute("create table PhoneBook (Name text, PhoneNum text);")
cur.execute("insert into PhoneBook values('Derick','010-222');")
name = "Conan"
phoneNumber = "010-333"
cur.execute("insert into PhoneBook values(?,?);",(name, phoneNumber))
# 한번에 여러 Row도 Insert가능
datalist = (('tom','010-123'),('dsp','010-456'))
cur.executemany("insert into PhoneBook values(?,?);", datalist)
# Select
cur.execute("select * from PhoneBook")
lst = cur.fetchall()
# lst = [('Derick', '010-222'), ('Conan', '010-333')...]
cur.fetchone()
# ('Derick', '010-222') 하나
>>> cur.fetchmany(2)
# [('Conan', '010-333'), ('tom', '010-123')] fetchmany안의 n개 만큼 출력
>>> cur.fetchall()
# [('dsp', '010-456')] fetch안에 존재하는 나머지 데이터 전부 출력
```

db파일 생성하여 데이터 fetch
```python
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
```
외부에서 db파일을 사용 가능
```python
con = sqlite3.connect("file_path_to\\file.db")
cur = con.cursor()
cur.execute("select * from PhoneBook")
for row in cur:
	print(row)
# ('derick', '010-222')
```