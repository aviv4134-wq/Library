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

def create_table():
    conn = get_connection()
    curs = conn.cursor()
    query = '''
    CREATE TABLE IF NOT EXISTS books(
     id           INT         AUTO_INCREMENT PRIMARY KEY,  
     title        VARCHAR(50)   NOT NULL,
     author       VARCHAR(50)   NOT NULL,
     genre        ENUM(Fiction, Non-Fiction, Science, History, Other)  NOT NULL,  
     is_available BOOLEAN    NOT NULL,                                        
     id_member_by_borrowed    INT        DEFAULT NULL                          
                      );
                      '''
    curs.execute('''CREATE TABLE IF NOT EXISTS books(
         id           INT         AUTO_INCREMENT PRIMARY KEY,  
         title        VARCHAR(50)   NOT NULL,
         author       VARCHAR(50)   NOT NULL,
         genre        ENUM(Fiction, Non-Fiction, Science, History, Other)  NOT NULL,  
         is_available             BOOLEAN    NOT NULL,                                        
         id_member_by_borrowed    INT        DEFAULT NULL  
                 )''')

# conn = get_connection()
# curs = conn.cursor()
# curs.execute('SHOW DATABASES;')
# print(curs.fetchall())
create_table()



