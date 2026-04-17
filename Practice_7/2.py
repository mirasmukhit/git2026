import psycopg2
def update_cursor(name,phone_number):
    conn = psycopg2.connect(
        dbname = "pp2_db",
        password = "081321",
        user = "postgres",
        host = "localhost"
    )
    cur = conn.cursor()
    cur.execute("DROP TABLE IF EXISTS users")
    cur.execute = ("""
        CREATE TABLE IF NOT EXISTS users(
            id SERIAL PRIMARY KEY,
            name VARCHAR(50) UNIQUE,
            phone_number VARCHAR(20)            
        )
            """)
    sql="""INSERT INTO users (name,phone_number) 
        VALUES (%s,%s)
        ON CONFLICT (name)
        DO UPDATE SET phone_number = EXCLUDED.phone_number"""
    cur.execute(sql,(name,phone_number))
    conn.commit()
    cur.close()
    conn.close()
conn = psycopg2.connect(
    dbname="pp2_db",
    user="postgres",
    password="081321",
    host="localhost"
)
cur = conn.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id SERIAL PRIMARY KEY,
        name VARCHAR(50) UNIQUE,
        phone_number VARCHAR(20)
    )
""")

cur.execute("INSERT INTO users (name, phone_number) VALUES (%s, %s)", ("Miras", "871146414198"))
conn.commit()

cur.close()
conn.close()
update_cursor("Miras", "87716766157")