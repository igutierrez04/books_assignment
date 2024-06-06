from flask_app.config.mysqlconnection import connectToMySQL


class Author:
    # Variable to store the name of the database we are connecting to
    DB = 'books_schema'
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']



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
