This read me contains some of the challanges i encountered while implement this exercise and how i overcomed it

problem: HOW TO GET THE LIBRARY ID FROM THE DJANGO SHELL
- enter into the django shell using the command
> python manage.py shell
- inside the shell we import the Library class and get the libraries object using the following commands
| from relationship_app.models import Library
| libraries = Library.objects.all() #get all libraries
| for library in libraries:
|     print(f"ID: {library.id}, Name: {library.name}")
- the output of the above command will list the library Id and library Name
thus we can use the library ID to get the library ID using the url 
> https://127.0.0.1:8000/relationship/library/1/