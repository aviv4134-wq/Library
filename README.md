Library Management System


the program will menage the library via fastapi server with http requests.
the program have a one database with two tables books and members.
the program will be able to read or change the data or add new data to the tables in the database via CRUD query.
the queries themselves going to bee in OOP 

frameworks and tools used to this program 
- Python
- FastAPI
- MySQL
- Docker


STRUCTURE FILES:

library-api/
│
│
├── main.py
├── database/
│ ├── db_connection.py
│ ├── book_db.py
│ └── member_db.py
├── routes/
│ ├── book_routes.py
│ ├── member_routes.py
│ └── report_routes.py
├── logs/
│ └── app.log
│
├── README.md
├── requirements.txt
└── .gitignore

DOCKER SETUP COMMANDS:
docker run --name mysql -e MYSQL_ROOT_PASSWORD=root -e MYSQL_DATABASE=library_db -p 3306:3306 -d mysql:8
enter to sql :
docker exec -it mysql mysql -uroot -proot

DATABASE:
library_db

TABLE: books


column name | data type     |  Constraints                                       |description
     id          INT         AUTO_INCREMENT PRIMARY KEY  
     title     VARCHAR(50)   NOT NULL
     author    VARCHAR(50)   NOT NULL
     genre     ENUM(Fiction, Non-Fiction, Science, History, Other)  NOT NULL,  #only allowed (Fiction, Non-Fiction,Science History  Other)
     available_is  BOOLEAN    NOT NULL  ,                                        #if false the book is borrowed
     id_member_by_borrowed    INT      DEFAULT NULL                              #the number id of member that borrowed the book 



TABLE: members


column name | data type     |  Constraints                                |description
     id          INT         AUTO_INCREMENT PRIMARY KEY,  
     name      VARCHAR(50)   NOT NULL,
     email     TEXT          NOT NULL   UNIQUE,
     is_active  BOOLEAN      NOT NULL                                      if false the member cant take a book  
     borrows_total  INT      AUTO_INCREMENT NOT NULL,                      every time the one of members borrow this counting by one 


SYSTEM RULES:

1:to create a book the book must have a title of the book and name of a author of the book and genre name and must be check by True or False if the book available.
only name title and name author that have 50 characters allowed else it will be error.
only one genre allowed from those genres (Fiction, Non-Fiction, Science, History, Other) else it will be error.

2: to create a member the member must have member name and an email of the member and check True or False if the member still active.
only name member that have 50 characters allowed else it will be error.
email must be unique from all others members email every email member must be unique else it will be error.

3:borrowing process:
when member try to borrowing a book the system will check:
   1: if the member is active? if the member active is False the system dont let him borrow if the member active is True the system will  continue to borrow book process and check the next step.
   2:if the member already borrowed 3 books the system dont let them borrow another one  
   3: if the book is already borrowed ? if the book is already borrowed the system dont let the member the book if the book is not already borrowed than the system give the book to the member
   

4:after member borrow a book system will do: 
  1: count borrow:
  every time member borrow a book the system count the number of borrowing
  2:check the is_active box False, that means the book is already borrowed
  3:the system take the id of the member that borrowed the book and save it to id_member_by_borrowed column in the database table

5:bring back a book
only the member who borrow the book in the first place can return the book  




ENDPOINT:

Books
Method Endpoint 
POST /books    #create a book
GET /books    #show all books
GET /books/{id}   ID  #show a book by id of the book 
PUT /books/{id}           #update a book by id of the book
PUT /books/{id}/borrow/{member_id}   #borrow a book to a friend by book id and member id
PUT /books/{id}/return/{member_id} #bring back a book from a friend by book id and member id 
Members
Method Endpoint 
members/ POST   #crate a member
members/ GET    #show members
GET /members/{id} ID  #show member by id 
PUT /members/{id}      #update a member by id member
PUT /members/{id}/deactivate  #disable a member by id member
PUT /members/{id}/activate  #active a member by id member
Reports
Method Endpoint 
GET /reports/summary  #show general report
GET /reports/books-by-genre #show all books group by genre
GET /reports/top-member show the most active member



HOW THE SYSTEM WORKS:
there is a fastapi server that listen to requests from client
when the user enter to an endpoint the server do the functions under the user entered endpoint 
then the function do connection to the mysql continer database 
and make a query to the mysql database 
and save the change or show the data of the database or error (depend of user endpoint request)
close the connection mysql database for security
and return the result of the request to the client

HOW TO RUN:
install venv
than do this in command line: pip install -r requirements.txt
go to main.py file use this in command line: uvicorn main:app --reload
then your server is up 
go to url http://127.0.0.1:8000/docs
and do requests