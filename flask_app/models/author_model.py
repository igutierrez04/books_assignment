from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import book_model


class Author:
    # Variable to store the name of the database we are connecting to
    DB = 'books_schema'
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.favorite_books = []
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.favorite_books = []



    @classmethod
    def create_author(cls, data):
        query = "INSERT INTO authors (name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW()); "
        return connectToMySQL(cls.DB).query_db(query, data)
    
    @classmethod
    def get_all_authors(cls):
        query = "SELECT * FROM authors;"
        results = connectToMySQL(cls.DB).query_db(query)
        # empty list to store authors
        authors = []
        # for loop to iterate over the db results and create an instance of each author
        for author in results:
            authors.append(cls(author))
        return authors
    
    @classmethod
    def get_one_author(cls, data):
        query = "SELECT * FROM authors WHERE authors.id = %(id)s;"
        results = connectToMySQL(cls.DB).query_db(query, data)
        return cls(results[0])

    @classmethod
    def unfavorited_authors(cls, data):
        query = "SELECT * FROM authors WHERE authors.id NOT IN (SELECT author_id FROM favorites WHERE book_id = %(id)s);"
        results = connectToMySQL(cls.DB).query_db(query, data)

        authors = []

        for db_data in results:
            authors.append(cls(db_data))
        return authors
    
    @classmethod
    def add_favorite(cls, data):
        query = "INSERT INTO favorites (author_id, book_id) VALUES (%(author_id)s, %(book_id)s); "
        return connectToMySQL(cls.DB).query_db(query, data)