# Import required modules && classes
from flask import Flask, Blueprint, render_template, request, redirect
from models.author import Author
from models.book import Book
import repositories.author_repository as author_repo
import repositories.book_repository as book_repo

# Create the Flask app
app = Flask(__name__)

# Register blueprints

author_blueprint = Blueprint('author', __name__)

# index
# GET - /authors
@author_blueprint.route('/authors')
def index():
    return render_template('authors/index.html')

# show
# GET - /authors/id 


# new
# GET - /authors/new

# create
# POST - /authors

# edit
# GET - /authors/id/edit

# update
# POST /authors/id

# delete
# POST - /authors/id/delete

app.register_blueprint(author_blueprint)

# Route home
@app.route('/')
def index():
    return render_template('index.html')

# __name__ == __main__
if (__name__ == '__main__'):
    app.run(debug=True)