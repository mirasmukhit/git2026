import psycopg2
def update_cursor(name,phone_number):
    conn = psycopg2.connect(
        dbname = "pp2_db",
        password = "081321",
        user = "postgres",
        host = "localhost"
    )
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id SERIAL PRIMARY KEY,
            name VARCHAR(50) UNIQUE,
            phone_number VARCHAR(20)            
        )
    """)
    sql="""
        INSERT INTO users (name,phone_number) 
        VALUES (%s,%s)
        ON CONFLICT (name)
        DO UPDATE SET phone_number = EXCLUDED.phone_number"""
    cur.execute(sql,(name,phone_number))
    conn.commit()
    cur.close()
    conn.close()
    return True
if(update_cursor("Edil", "871146414198")):
    print("Added")
if(update_cursor("Edil", "87716766157")):
    print("Updated")
conn = psycopg2.connect(
        dbname = "pp2_db",
        password = "081321",
        user = "postgres",
        host = "localhost"
    )
cur = conn.cursor()
cur.execute("SELECT * FROM users")
for row in cur.fetchall():
    print(row)