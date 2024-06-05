from flask_app import app
from flask import render_template, redirect, request
from flask_app.models.author_model import Author
from flask_app.models.book_model import Book

@app.route('/')
def index():
    return redirect('/authors')

@app.route('/authors')
def authors():
    return render_template('authors.html', authors = Author.get_all_authors())

@app.route('/create/author', methods=['POST'])
def create_author():
    Author.create_author(request.form)
    return redirect('/authors')

@app.route('/show/author/<int:id>')
def show_author(id):
    data = {
        'id': id
    }
    return render_template('author_page.html', author = Author.get_one_author(data))