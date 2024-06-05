from flask_app.config.mysqlconnection import connectToMySQL

class Book:
    # Variable to store the name of the database we are connecting to
    DB  = 'books_schema'

    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

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