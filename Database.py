import sqlite3 as sql

"""SQLite is a C library that provides a lightweight disk-based database that doesn’t require a separate server process and allows accessing the database using a nonstandard variant of the SQL query language. Some applications can use SQLite for internal data storage. It’s also possible to prototype an application using SQLite and then port the code to a larger database such as PostgreSQL or Oracle."""

# create database
con = sql.connect("database")

cur = con.cursor()
cur.execute("CREATE TABLE employee(name,age)")
cur.execute("INSERT INTO employee VALUES(?,?)",("rohan",45))
con.commit()
con.close()