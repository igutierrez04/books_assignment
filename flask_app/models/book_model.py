from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import author_model

class Book:
    # Variable to store the name of the database we are connecting to
    DB  = 'books_schema'

    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        # list of authors who has favorited this book
        self.authors_who_favorited = []

    @classmethod
    def create_book(cls, data):
        query = "INSERT INTO books (title, num_of_pages, created_at, updated_at) VALUES (%(title)s, %(num_of_pages)s, NOW(), NOW()); "
        return connectToMySQL(cls.DB).query_db(query, data)
    
    @classmethod
    def get_all_books(cls):
        query = "SELECT * FROM books;"
        results = connectToMySQL(cls.DB).query_db(query)
        # empty list to store books
        books = []
        # for loop to iterate over the db results and create an instance of each book
        for book in results:
            books.append(cls(book))
        return books
    
    @classmethod
    def get_book_id(cls, data):
        query = "SELECT * FROM books LEFT JOIN favorites ON books.id = favorites.book_id LEFT JOIN authors ON authors.id = favorites.author_id WHERE books.id = %(id)s; "
        results = connectToMySQL(cls.DB).query_db(query, data)
        
        book = cls(results[0])

        for db_data in results:
            if db_data['authors.id'] == None:
                break
            data = {
                "id": db_data['authors.id'],
                "name": db_data['name'],
                "created_at": db_data['created_at'],
                "updated_at": db_data['updated_at']
            }
            book.authors_who_favorited.append(author_model.Author(data))
        return book