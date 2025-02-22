**This read me contains some of the challanges I encountered while implementing this exercise and how to go about it.**

## 2. HOW TO GET THE LIBRARY ID FROM THE DJANGO SHELL
 - Enter into the **django shell** :shell: using the command python manage.py shell
 - Inside the shell we import the Library class and use the get() method to obtain all the libraries
 ```terminal
>>> from relationship_app.models import Library
>>> libraries = Library.objects.all()
>>> for library in libraries:
...     print(f"ID: {library.id}, Name: {library.name}")

 ```
 - the output of the above command will list the library Id and library Name :computer:
 ```
 ID: 1, Name: Central Library
 ID: 2, Name: Central Library
 ```
 thus we can use the library ID to get the library ID using the url 

![image of django shell](/django-models/LibraryProject/screenshot/django-shell.png)

- enter the following url in the browser to see the library :smile:
<https://127.0.0.1:8000/relationship/library/1/>

![image of the url opened in a browser](/django-models/LibraryProject/screenshot/image_in_browser.png)

## 3. HANDLING THE CACHE FILES.
python interpreter executes the **.py** files and compiles them into bytecode stored in the __pycache__ directory as **.pyc** file. This helps to improve the speed of execution of the code, so the next time the python file is run, python execute the bytecode without needing to recompile the code.

- use this command if you want to delete the cache file
'''
find . -name "__pycache__" -exec rm -r {} +
'''