import mysql.connector

connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Yuvi@12345",
    database = "sql_hr"
)

# Get user input for the word
word = input("Enter a word: ")

# Create the SQL query dynamically
sql_query = f"""
WITH RECURSIVE SplitWord AS (
    SELECT SUBSTRING('{word}', 1, 1) AS Character, 1 AS Position
    UNION ALL
    SELECT SUBSTRING('{word}', Position + 1, 1), Position + 1
    FROM SplitWord
    WHERE Position < LENGTH('{word}')
)
SELECT Character FROM SplitWord;
"""

# Execute the SQL query
cursor = connection.cursor()
cursor.execute(sql_query)

# Fetch and print the results
rows = cursor.fetchall()
for row in rows:
    print(row[0])

# Close the cursor and connection
cursor.close()
connection.close()