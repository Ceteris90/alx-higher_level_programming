#!/usr/bin/python3
import mysql.connector

# Establish a connection to the MySQL server
cnx = mysql.connector.connect(
    host='localhost',
    user='your_username',
    password='your_password'
)

# Create a cursor object to execute SQL queries
cursor = cnx.cursor()

# Execute the query to retrieve all databases
cursor.execute("SHOW DATABASES")

# Fetch all the database names from the result set
database_names = [row[0] for row in cursor]

# Print the list of databases
for database_name in database_names:
    print(database_name)

# Close the cursor and connection
cursor.close()
cnx.close()
