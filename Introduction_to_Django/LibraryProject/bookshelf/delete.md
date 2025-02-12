4. delete.md
here are the steps to DELETE a book instance form the Book class
- enter the command in the django shell
""" 
>>> book = Book.objects.get(title="Nineteen Eighty-Four")
>>> book.delete()

"""
output: (1, {'bookshelf.Book': 1}) 
