import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='sharukesh',
    passwd='1234',
    auth_plugin='mysql_native_password'  # Specify the authentication plugin
)

my_cursor = mydb.cursor()

# Create the database
my_cursor.execute("CREATE DATABASE IF NOT EXISTS USERS")

# Select the newly created database
my_cursor.execute("USE USERS")

# Show databases
my_cursor.execute("SHOW DATABASES")

# Fetch all databases and print them
databases = my_cursor.fetchall()
for db in databases:
    print(db)