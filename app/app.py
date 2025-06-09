import sqlite3
user_input = input("Enter username: ")
query = "SELECT * FROM users WHERE username = '" + user_input + "'"
conn = sqlite3.connect('app.db')
cursor = conn.cursor()
cursor.execute(query)