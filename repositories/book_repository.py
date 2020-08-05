# Import modules
from db.run_sql import run_sql
from models.book import Book
from models.author import Author
import repositories.author_repository as author_repo

# Functions

def select_all():
    # make a list of books == empty list
    books = []

    # create the sql query
    sql = 'SELECT * FROM books'
    results = run_sql(sql)

    # loop through results
    for row in results:
        author = author_repo.select_author_by(row['author_id'])
        new_book = Book(row['title'], row['release_date'], author, row['id'])
        books.append(new_book)
    return books

def select_book_by(id):
    # create the sql query
    sql = 'SELECT * FROM books WHERE id = %s'
    values = [id]
    result = run_sql(sql, values)

    # Create a new book object if a result is returned from db
    if len(result) > 0:
        author = author_repo.select_author_by(result[0]['author_id'])
        new_book = Book(result[0]['title'], result[0]['release_date'], author, result[0]['id'])
        return new_book

def delete_book_by(id):
    # create the sql query
    sql = 'DELETE FROM books WHERE id = %s'
    values = [id]
    run_sql(sql, values)