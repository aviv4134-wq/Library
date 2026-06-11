import mysql.connector


def connection_get():
    conn =  mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'root',
        port = 3306,
        database = 'library_db'
    )
    return conn


    






