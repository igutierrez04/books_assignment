from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.book_model import Book
from flask_app.models.author_model import Author

@app.route('/book')
def book():
    return render_template('books.html', books = Book.get_all_books() )

@app.route('/create/book', methods = ['POST'])
def create_book():
    data = {
        'title': request.form['title'],
        'num_of_pages': request.form['num_of_pages']
    }
    book_id = Book.create_book(data)
    return redirect('/book')

@app.route('/book/<int:id>')
def show_book(id):
    data = {
        'id': id
    }
    return render_template('book_page.html', book = Book.get_book_id(data), unfavorited_authors = Author.unfavorited_authors(data))

@app.route('/favorite/book', methods=['POST'])
def favorite_book():
    data = {
        'author_id': request.form['author_id'],
        'book_id': request.form['book_id']
    }
    Author.add_favorite(data)
    return redirect(f'/book/{request.form["book_id"]}')