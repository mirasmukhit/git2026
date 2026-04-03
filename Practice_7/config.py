DB_CONFIG = {
    "host": "localhost",
    "dbname": "pp2_db",
    "user": "postgres",
    "password": "secret"
}



import psycopg2
conn = psycopg2.connect(**DB_CONFIG)