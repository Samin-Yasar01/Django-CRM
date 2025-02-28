import MySQLdb

# Connect to MySQL
dataBase = MySQLdb.connect(
    host="localhost",
    user="root",
    passwd="1020444745xD"
)

# Create a cursor object
cursorObject = dataBase.cursor()

# Execute the query to create a database
cursorObject.execute("CREATE DATABASE IF NOT EXISTS elderco")

# Commit the changes
dataBase.commit()

# Close the connection
#cursorObject.close()
#dataBase.close()

print("All Done!")