import sqlite3
import pandas as pd

conn = sqlite3.connect('sqlite_app_codemy/example.sqlite')
c = conn.cursor()

c.execute("SELECT * FROM customers2")

items = c.fetchall()

#for item in items:
#    print(item)

conn.commit()

conn.close()

df = pd.DataFrame(items)

print(df)