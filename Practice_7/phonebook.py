import psycopg2
import csv
conn = psycopg2.connect(
    host = "localhost",
    dbname = "pp2_db",
    user = "postgres",
    password = "081321"
)
cur = conn.cursor()
cur.execute("""
            CREATE TABLE IF NOT EXISTS phonebook (
        id SERIAL PRIMARY KEY,
        name       VARCHAR(100)     NOT NULL,
        email       VARCHAR(100)    NOT NULL,
        phone_number    VARCHAR(100)    UNIQUE NOT NULL);
            """)
with open("Practice_7/contacts.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)  # skip header

    for row in reader:
        cur.execute("""
            INSERT INTO phonebook (name, email, phone_number)
            VALUES (%s, %s, %s)
            ON CONFLICT DO NOTHING;
        """, row)
conn.commit()
print("Table created")
cur.close()
conn.close()