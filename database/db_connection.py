import mysql.connector


def get_connection():
    conn =  mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'root',
        port = 3306,
        database = 'library_db'
    )
    return conn

    






