import psycopg2
conn = psycopg2.connect(
    host="localhost",
    dbname="pp2_db",
    user="postgres",
    password="secret"
)

cur = conn.cursor()

phone = input("Enter phone number: ")
new_name = input("Enter new name: ")

cur.execute(
    "UPDATE phonebook SET name = %s WHERE phone_number = %s RETURNING*;",
    (new_name, phone)
)

rows = cur.fetchall()
conn.commit()
print("--- Updated Phonebook Table ---")
cur.execute("SELECT * FROM phonebook;") 
rows = cur.fetchall()                   

for row in rows:                        
    print(row)

cur.close()
conn.close()