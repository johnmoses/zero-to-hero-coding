""" 
Getting started
"""
import psycopg2
def get_connection():
    try:
        return psycopg2.connect(
            database="demodb",
            user="postgres",
            password="demo_pass",
            host="127.0.0.1",
            port=5432,
        )
    except:
        return False
conn = get_connection()
if conn:
    print("Connection to the PostgreSQL established successfully.")
else:
    print("Connection to the PostgreSQL encountered and error.")