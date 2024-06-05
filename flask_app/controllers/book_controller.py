from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.book_model import Book
from flask_app.models.author_model import Author

@app.route('/book')
def book():
    return render_template('books.html', books = Book.get_all_books() )

@app.route('/create/book', methods = ['POST'])
def create_book():
    Book.create_book(request.form)
    return redirect('/book')