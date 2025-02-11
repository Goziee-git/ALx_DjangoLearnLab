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

2. retrieve.md
here are the steps to retrieve a book instance from the Book class
- in th django shell enter the following commands
"""
>>> book = Book.objects.get(title="1984")
>>> print(book.title, book.author, book.publication_year)

"""
output: 1984 Geroge Orwell 1949

3. update.md
here are the steps to perform an UPDATE operation on the Book class
- insert into the django interactive shell this commands;
"""
>>> book = Book.objects.get(title="1984")
>>> book.title = "Nineteen Eighty-Four"
>>> book.save()
>>> print(book.title)

"""
output: Nineteen Eighty-Four

4. delete.md
here are the steps to DELETE a book instance form the Book class
- enter the command in the django shell
""" 
>>> book = Book.objects.get(title="Nineteen Eighty-Four")
>>> book.delete()

"""
output: (1, {'bookshelf.Book': 1})