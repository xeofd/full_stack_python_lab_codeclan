# Import required modules && classes
from flask import Flask, Blueprint, render_template, request, redirect
from models.author import Author
from models.book import Book
import repositories.author_repository as author_repo
import repositories.book_repository as book_repo


author_blueprint = Blueprint('author', __name__)

# index
# GET - /authors
@author_blueprint.route('/authors')
def authors_index():
    authors = author_repo.select_all()
    return render_template('author/index.html', title='Authors', authors=authors)

# show
# GET - /authors/id 
@author_blueprint.route('/authors/<id>')
def view_author(id):
    author = author_repo.select_author_by(id)
    return render_template('author/show.html', title=author.first_name+" "+author.last_name, author=author)

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
@author_blueprint.route('/authors/<id>/delete', methods=['POST'])
def delete_author(id):
    author_repo.delete_author_by(id)
    return redirect('/authors')