#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sqlite3
# Connect to the SQLite database or create one if it doesn't exist
conn = sqlite3.connect('ages.sqlite')
cur = conn.cursor()

# Create the table "Ages" if it doesn't exist
cur.execute('''CREATE TABLE IF NOT EXISTS Ages (
                name VARCHAR(128),
                age INTEGER)''')

# Delete any existing rows in the table
cur.execute('DELETE FROM Ages')

# Insert rows into the table
cur.execute("INSERT INTO Ages (name, age) VALUES ('Mara', 28)")
cur.execute("INSERT INTO Ages (name, age) VALUES ('Otto', 33)")
cur.execute("INSERT INTO Ages (name, age) VALUES ('Fyn', 31)")
cur.execute("INSERT INTO Ages (name, age) VALUES ('Neshawn', 17)")

# Retrieve the rows with hex encoded values
cur.execute("SELECT hex(name || age) AS X FROM Ages ORDER BY X")

# Fetch the first row
row = cur.fetchone()
print("The first row in the resulting record set:", row[0])

# Commit changes and close connection
conn.commit()
cur.close()


# In[ ]:




