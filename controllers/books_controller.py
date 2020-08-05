# Import required modules && classes
from flask import Flask, Blueprint, render_template, request, redirect
from models.author import Author
from models.book import Book
import repositories.author_repository as author_repo
import repositories.book_repository as book_repo


book_blueprint = Blueprint('book', __name__)

# index
# GET - /books
@book_blueprint.route('/books')
def book_index():
    books = book_repo.select_all()
    return render_template('book/index.html', title='Books', books=books)

# show
# GET - /books/id 
@book_blueprint.route('/books/<id>')
def view_book(id):
    book = book_repo.select_book_by(id)
    return render_template('/book/show.html', title=book.title, book=book)

# new
# GET - /books/new
@book_blueprint.route('/books/add')
def add_book():
    authors = author_repo.select_all()
    return render_template('/book/add.html', title='Add a book', authors=authors)

# create
# POST - /books
@book_blueprint.route('/books', methods=['POST'])
def add_book_to_db():
    title = request.form['title']
    release_date = request.form['date']
    author_id = request.form['author']

    author = author_repo.select_author_by(author_id)

    new_book = Book(title, release_date, author)
    book_repo.save(new_book)

    return redirect('/books')

# edit
# GET - /books/id/edit

# update
# POST /books/id

# delete
# POST - /books/id/delete
@book_blueprint.route('/books/<id>/delete', methods=['POST'])
def delete_author(id):
    book_repo.delete_book_by(id)
    return redirect('/books')