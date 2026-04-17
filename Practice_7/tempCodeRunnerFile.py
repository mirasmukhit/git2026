import psycopg2
conn=psycopg2.connect(
    db_name = "pp2_db",
    password = "081321",
    user = "postgers",
    host = "localhost"
)
cur = conn.cursor()
cur.execute(
    "SELECT phone_number WHERE name = %s",
    ("Miras",)
)
for row in cur.fetchall():
    print(row)
cur.close()
conn.close()