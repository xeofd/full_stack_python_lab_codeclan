# Import modules
from db.run_sql import run_sql
from models.book import Book
from models.author import Author

# Functions

def select_all():
    # Create authors == empty list
    authors = []
    # Create the sql query
    sql = 'SELECT * FROM authors'
    results = run_sql(sql)

    # Loop through the results
    for row in results:
        new_author = Author(row['first_name'], row['last_name'], row['id'])
        authors.append(new_author)
    
    return authors

def select_author_by(id):
    # Create the sql query
    sql = 'SELECT * FROM authors WHERE id = %s'
    values = [id]
    result = run_sql(sql, values)

    # Create a new author object if a result is returned from db
    if len(result) > 0:
        new_author = Author(result[0]['first_name'], result[0]['last_name'], result[0]['id'])
        return new_author

def delete_author_by(id):
    # Create the sql query
    sql = 'DELETE FROM authors WHERE id = %s'
    values = [id]
    run_sql(sql, values)