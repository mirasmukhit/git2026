import psycopg2
from config import  DB_CONFIG

def get_connection():
    try:
        return psycopg2.connect(**DB_CONFIG)
    except Exception as e: #if something goes wrong!(wrong password or server not running)
        print(f"Database connection error: {e}")#it catches error
        return None