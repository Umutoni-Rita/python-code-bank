import sqlite3

conn = sqlite3.connect('Users.db')
cur = conn.cursor()

# cur.execute('CREATE TABLE practice(fname VARCHAR(100), email VARCHAR(100), id INTEGER PRIMARY KEY autoincrement)')
# name = input('Enter your name: ')
# email = input('Enter your email: ')

# cur.execute(f"INSERT INTO practice (fname, email) VALUES ('{name}', '{email}')")

result = cur.execute("SELECT fname, email FROM practice WHERE id <= 3")


for row in result:
    print(row)

conn.commit()
conn.close()



























# import sqlite3

# #Creating connection and cursor
# conn = sqlite3.connect('Users.db') #connection object
# cur = conn.cursor()


# ##CREATING TABLE
# cur.execute('DROP TABLE IF EXISTS Users')
# cur.execute('CREATE TABLE Users(fname VARCHAR(128), lname VARCHAR(128), email VARCHAR(128))')

# fname = input('Enter first name: ')
# lname = input('Enter last name: ')
# email = input('Enter email: ')
# cur.execute('''
#             INSERT INTO Users (fname, lname, email) VALUES (?, ?, ?)''',
#             (fname, lname, email))
# conn.commit()
# cur.close()