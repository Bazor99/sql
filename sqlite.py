import sqlite3

##connect to SQlite
connection=sqlite3.connect('student.db')

## create cursor object to insert record, create table

cursor=connection.cursor()

## create table

table_info="""
CREATE TABLE student(NAME VARCHAR(25),CLASS VARCHAR(25),SECTION VARCHAR(25));

"""

cursor.execute(table_info)

## insert some more records
cursor.execute('''INSERT INTO student VALUES('Sam','science','A')''')
cursor.execute('''INSERT INTO student VALUES('Dabra','science','B')''')
cursor.execute('''INSERT INTO student VALUES('Leo','science','A')''')
cursor.execute('''INSERT INTO student VALUES('Gab','Dev','A')''')
cursor.execute('''INSERT INTO student VALUES('Jon','Dev','B')''')

## display All the records
print("The inserted records are")
data=cursor.execute('''select * from student''')
for row in data:
    print(row)


##commit your chages in the database

connection.commit()
connection.close()



