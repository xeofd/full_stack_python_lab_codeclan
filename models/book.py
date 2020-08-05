# New class: Book
# Creates a book object with an ID, title, release date and an author

class Book:
    # initialise the class
    def __init__(self, title, release_date, author, id=None):
        self.title = title
        self.release_date = release_date
        self.author = author
        self.id = id