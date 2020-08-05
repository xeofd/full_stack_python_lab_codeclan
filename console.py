# Import modules
import pdb
from models.author import Author
from models.book import Book
import repositories.author_repository as author_repo
import repositories.book_repository as book_repo

# Add some data to db

author1 = Author('JK', 'Rowling')
author2 = Author('George', 'Orwell')
author3 = Author('Charles', 'Dickens')

author_repo.save(author1)
author_repo.save(author2)
author_repo.save(author3)

book1 = Book('Harry Potter and the Goblet of Fire', '08/07/2000', author1)
book_repo.save(book1)

book2 = Book('Harry Potter and the Chamber of Secrets', '02/07/1998', author1)
book_repo.save(book2)

book3 = Book('1948', '08/06/1949', author2)
book_repo.save(book3)

book4 = Book('Christmas Carol', '01/01/1843', author3)
book_repo.save(book4)