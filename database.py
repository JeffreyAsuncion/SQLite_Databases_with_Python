import sqlite3

# conn = sqlite.connect(':memory:')   # to create a database in memory that disappear after done
conn = sqlite3.connect('customer.db')


# before create table need a cursor
# Create a cursor
cursor = conn.cursor()

# Insert into database
cursor.execute("INSERT INTO customers VALUES ('John', 'Elder', 'john@codemy.com')")

# Commit our command
conn.commit()

# Close our connection
conn.close()
