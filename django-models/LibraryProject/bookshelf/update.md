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