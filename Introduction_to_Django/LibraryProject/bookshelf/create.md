1. create.md
here are the steps to create a book instance from the django shell
- start the shell using the command < python manage.py shell > on the terminal
- in the django shell enter the following commands 
"""
>>> from bookshelf.models import Book
>>> book = Book.objects.create(title="1984", author="George Orwell", publication_year="1949)
>>> print(book)

"""
output: 1984