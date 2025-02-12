4. delete.md
here are the steps to DELETE a book instance form the Book class
""" 

- enter the django shell using the command
>>> python manage.py shell
- import Book class using the syntax ["from bookshelf.models import Book"]
>>> from bookshelf.models import Book
- enter the command in the django shell
>>> book = Book.objects.get(title="Nineteen Eighty-Four")
>>> book.delete()

"""
output: (1, {'bookshelf.Book': 1}) 
