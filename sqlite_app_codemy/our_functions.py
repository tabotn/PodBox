import sqlite3
# connect to database
conn = sqlite3.connect('sqlite_app_codemy/example.sqlite')
# create a cursor
c = conn.cursor()

# Query the database and return all records


def show_all():
    # connect to database
    conn = sqlite3.connect('sqlite_app_codemy/example.sqlite')
    # create a cursor
    c = conn.cursor()
    # Query the database
    c.execute("SELECT rowid, * FROM customers2")
    items = c.fetchall()

    for item in items:
        print(item)

    conn.commit()
    conn.close()


# Add a new record to the table
def add_one(first, last, email):
    conn = sqlite3.connect('sqlite_app_codemy/example.sqlite')
    c = conn.cursor()
    c.execute("INSERT INTO customers2 VALUES (?,?,?)", (first, last, email))

    conn.commit()
    conn.close()


def delete_one(id):
    conn = sqlite3.connect('sqlite_app_codemy/example.sqlite')
    c = conn.cursor()

    c.execute("DELETE FROM customers2  WHERE rowid = (?)", id)

    conn.commit()
    conn.close()


def add_many(list):
    conn = sqlite3.connect('sqlite_app_codemy/example.sqlite')
    c = conn.cursor()
    c.executemany("INSERT INTO customers2 VALUES (?,?,?)", (list))

    conn.commit()
    conn.close()
