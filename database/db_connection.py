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

def create_table() -> str:
        try:
            conn = get_connection()
            curs = conn.cursor()
            query_create_books_table = '''
            CREATE TABLE IF NOT EXISTS books(
                    id           INT         AUTO_INCREMENT PRIMARY KEY,  
                    title        VARCHAR(50)   NOT NULL,
                    author       VARCHAR(50)   NOT NULL,
                    genre        ENUM('Fiction','Non-Fiction','Science','History','Other')  NOT NULL,  
                    is_available             BOOLEAN    NOT NULL,                                        
                    id_member_by_borrowed    INT        DEFAULT NULL  
                            )'''
            query_create_members_table = '''
                CREATE TABLE IF NOT EXISTS members(
                id          INT         AUTO_INCREMENT PRIMARY KEY,  
                name        VARCHAR(50)   NOT NULL,
                email       VARCHAR(255)     NOT NULL   UNIQUE,
                is_active   BOOLEAN      NOT NULL,                                        
                borrows_total  INT       NOT NULL                    
                                )'''                
            curs.execute(query_create_books_table)
            curs.execute(query_create_members_table)
            return 'the tables created '
        except Exception as error:
             return f'error not created \n {error}'            



if __name__  == '__main__':
    print(get_connection())
    print(create_table())