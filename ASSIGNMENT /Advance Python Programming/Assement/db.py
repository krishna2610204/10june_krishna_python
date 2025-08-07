import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",     # Use your actual password if set
        database="bank_db",
        port=3306
    )
