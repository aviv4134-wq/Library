from db_connection import get_connection



class BookDB:
    def create_book(self,data):   #check if book exists 404
        try:
            conn = get_connection()
            curs = conn.cursor()
            data_values = tuple(data.values())
            query_find_book = '''
            SELECT * FROM books 
            WHERE title = %s AND author = %s AND genre = %s'''
            curs.execute(query_find_book,data_values)
            book = curs.fetchone()
            if book:
                return None 
            query = '''
            INSERT INTO books (title,author,genre)
            VALUES(%s,%s,%s)
            '''
            curs.execute(query,data_values)
            conn.commit()
            return 'success to create a book'
        except :
            return None
        finally:
            curs.close()
            curs.close()


    def get_all_books(self):
        conn = get_connection()
        curs = conn.cursor(dictionary=True)
        query = '''
        SELECT * FROM books     
        '''
        curs.execute(query)
        books = curs.fetchall()
        curs.close()
        conn.close()
        return books

    def get_book_by_id(self,id):
        conn = get_connection()
        curs = conn.cursor(dictionary=True)
        query ='''
        SELECT * FROM books WHERE id = %s     
        '''
        book_id = (id,)
        curs.execute(query,book_id)
        book = curs.fetchone()
        curs.close()
        conn.close()
        if book:
            return book
        return None

    def books_total_count(self):
        conn = get_connection()
        curs = conn.cursor()
        query ='''
        SELECT COUNT(*) FROM books     
            '''
        curs.execute(query)
        books_count = curs.fetchone()
        books_count = books_count[0]
        curs.close()
        conn.close()
        return books_count

    def count_available_books(self):
        conn = get_connection()
        curs = conn.cursor()
        query ='''
        SELECT COUNT(*) FROM books WHERE available_is = TRUE   
        '''
        curs.execute(query)
        books_count_available = curs.fetchone()
        books_count_available = books_count_available[0]  
        curs.close()
        conn.close()
        return books_count_available

    def count_borrowed_books(self):
        conn = get_connection()
        curs = conn.cursor()
        query ='''
        SELECT COUNT(*) FROM books WHERE is_available = FALSE   
        '''
        curs.execute(query)
        books_count_available = curs.fetchone()
        books_count_available = books_count_available[0]  
        curs.close()
        conn.close()
        return books_count_available

    def count_by_genre(self,genre):
        conn = get_connection()
        curs = conn.cursor()
        query ='''
        SELECT COUNT(*) FROM books WHERE genre = %s    
        '''
        genre = (genre,)
        curs.execute(query,genre)
        books_count_by_genre = curs.fetchone()
        books_count_by_genre = books_count_by_genre[0]  
        curs.close()
        conn.close()
        return books_count_by_genre

    def update_book(self,id, data):
        try:
            conn = get_connection()
            curs = conn.cursor()
            columns = [ f'{key} = %s' for key in data.keys()]
            columns = ', '.join(columns)
            values = list(data.values()) + [id]           
            query = f'''UPDATE books SET {columns}
            WHERE id = %s 
            '''
            curs.execute(query,values)
            if curs.rowcount > 0:
                conn.commit()
                return 'update complete'
            return None
        except:
            return None
        finally:
            curs.close()
            conn.close()
                            
            
    def set_available(self,id, val,member_id):
            conn = get_connection()
            curs = conn.cursor()
            if val :
               return_query = '''
               UPDATE books SET is_available = TRUE, borrowed_by_member_id = NULL
               WHERE id = %s
               '''
               curs.execute(return_query,(id,))
            else:
                borrowed_book_query = '''
                UPDATE books SET is_available = FALSE, borrowed_by_member_id = %s
                WHERE id = %s
                '''
                curs.execute(borrowed_book_query,(member_id,id))
                update_member ='''
                UPDATE members SET total_borrows = total_borrows + 1 WHERE id = %s
                '''
                curs.execute(update_member,(member_id,))
            conn.commit()
            curs.close()
            conn.close()
            return 'update completed'

    def count_active_borrows_by_member(self,member_id):
        conn = get_connection()
        curs = conn.cursor()
        query = '''
        SELECT COUNT(*) FROM books
        WHERE borrowed_by_member_id = %s
        '''
        member_id = (member_id,)
        curs.execute(query,member_id)
        active_borrows_count =  curs.fetchone()
        active_borrows_count = active_borrows_count[0]
        return active_borrows_count
        
         
           
       
if __name__  == '__main__':
    b = BookDB()
    d =    {
    "title": "Thef Hitchhiker's Guide to the Galaxy",
    "author": "Douglas Adams",
    "genre": "Fiction"
    }

    #print(b.create_book(d))
    #print(b.update_book(1,d))
    #print(b.set_available(2,False,2))
    #print(b.count_active_borrows_by_member(2))
    print(b.count_by_genre('gfdgdgf'))