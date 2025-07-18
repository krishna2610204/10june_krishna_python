import sqlite3

try:
    con=sqlite3.connect("demo.db")
    print("Database created")
except Exception as e:
    print(e)

#Table Created
table_create = "create table studinfo(id integer primary key autoincrement , name text , city text)"
try:
    con.execute(table_create)
    print("Table Created")
except Exception as e:
    print(e)

#Insert Data
insert_data = "insert into studinfo(name,city) values ('Krishna','Rajkot'), ('Vrinda','Rampur'), ('Trisha','Ahmedabad'),('Diya','Surat'),('Riya','Jamnagar')"
try:
    con.execute(insert_data)
    print("Record Inserted")
    con.commit()
except Exception as e:
    print(e)

#Update Data
update = "update studinfo set city = 'Rajkot' where id = 2" 
try:
    con.execute(update)
    print("Table Update")
    con.commit()
except Exception as e:
    print(e)

#Delete
delete = "delete from studinfo where id = 2"
try:
    con.execute(delete)
    print("Table Deleted")
    con.commit()
except Exception as e:
    print(e)