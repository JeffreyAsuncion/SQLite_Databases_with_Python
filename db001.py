import sqlite3

# conn = sqlite.connect(':memory:')   # to create a database in memory that disappear after done
conn = sqlite3.connect('customer.db')


# before create table need a cursor
# Create a cursor
cursor = conn.cursor()

# Create a table
cursor.execute("""CREATE TABLE customers (
                    first_name TEXT,
                    last_name TEXT,
                    email TEXT
    )""")

# Datatypes:
# NULL
# INTEGER
# REAL
# TEXT
# BLOB (mp3,etc)

# Commit our command
conn.commit()

# Close our connection
conn.close()
