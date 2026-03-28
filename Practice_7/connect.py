import psycopg2

conn = psycopg2.connect(
    host="localhost",
    dbname="pp2_db",
    user="postgres",
    password="081321",
    port="5432"
)

cur = conn.cursor()
print("Connected!")

cur.close()
conn.close()
