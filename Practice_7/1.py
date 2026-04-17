import psycopg2
import csv
conn=psycopg2.connect(
    dbname = "pp2_db",
    password = "081321",
    user = "postgres",
    host = "localhost"
)
cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS users(
            id SERIAL PRIMARY KEY,
            name VARCHAR(50),
            phone_number VARCHAR(20)
    )
""")
cur.execute("INSERT INTO users (name,phone_number) values (%s,%s)",("Miras","874787948485"))

conn.commit
cur.execute(
    "SELECT phone_number FROM users WHERE name = %s",
    ("Miras",)
)
for row in cur.fetchall():
    print(row)
cur.close()
conn.close()