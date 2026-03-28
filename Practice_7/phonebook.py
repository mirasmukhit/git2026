import psycopg2
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
cur.execute("""
insert into phonebook(name,email,phone_number)
            values('Aaa','a@gmail.com','8777777'),
            ('Bbb','b@gmail.com',8887777);
""")
conn.commit()
print("Table created")
cur.close()
conn.close()