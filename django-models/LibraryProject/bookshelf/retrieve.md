2. retrieve.md
here are the steps to retrieve a book instance from the Book class
- in th django shell enter the following commands
"""
>>> from book.models import Book
- note: the book object must be created before it can be retrieved using this command ["Book.objects.get", "1984"]
>>> book = Book.objects.get(title="1984")
>>> print(book.title, book.author, book.publication_year)

"""
output: 1984 Geroge Orwell 1949