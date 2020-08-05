# Import required modules && classes
from flask import Flask, Blueprint, render_template, request, redirect
from controllers.authors_controller import author_blueprint
from controllers.books_controller import book_blueprint
import repositories.author_repository as author_repo
import repositories.book_repository as book_repo

# Create the Flask app
app = Flask(__name__)

# Register blueprints

app.register_blueprint(author_blueprint)
app.register_blueprint(book_blueprint)

# Route home
@app.route('/')
def index():
    books = book_repo.select_all()
    authors = author_repo.select_all()
    return render_template('index.html', title='Home', books=books, authors=authors)

# __name__ == __main__
if (__name__ == '__main__'):
    app.run(debug=True)