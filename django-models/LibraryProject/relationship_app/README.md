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

 find . -name "__pycache__" -exec rm -r {} +

## class based vs function based views
class based views implement django vieww as classes with several fields and methods that are uses to handle all kinds of HTTP request and respose. Function based views on the other hand implement the views as simple functions to implement views
- for the class based views, each class represents a view that in some cases inherit from the generic django built in views such as DetailView, ListView, UpdateView, CreateView, DeleteView, FormView, TemplateView
- to use any of the generic views we have to import it using 
>> from django.views.generic import <genericviewtype>
- when we define this views that inherits fromt the built-in generic views as a class, as with classes we have to define class attributes and methoods( to handle HTTP request and response) some examples of these class attributes include
model, template_name, context_object_name, paginate_by, ordering, queryset, fields, success_url, form_class, login_url

## accessing the URls defined 
- for the ListBookView
http://127.0.0.1:8000/relationship/books/
- shows all books using list_books.html template
http://127.0.0.1:8000/relationship/library/1/ 
1 can be replaced with the actuall library ID
- registeration page URL using the register.html
http://127.0.0.1:8000/relationship/register/
- login page URL using the login.html
http://127.0.0.1:8000/relationship/login/
** - the login page URL is protected by the login_required decorator, so you can't access it without logging
- the logout URL : note that if we use the url like this http://127.0.0.1:8000/relationship/logout/ it will not work because this performs a GET request, However for security reasons, logout operations should use a POST requests to prevent CSRF (Cross-Site Request Forgery) attacks. CSRF is a security mechanism that generates a unique token for each user session, token must be included with the POST requests to verify they come from your site, helping to prevent attacker from tricking users onto submitting malicious requests. to this end, django generates a unique token, stores it in the user's session, includes it as a hidden form field, verifies the token when processing POST requests
>> Remember: You should always access the logout functionality through a POST request (using the form), not by directly visiting the URL.
- using admin.html, requires admin role ## correct this
http://127.0.0.1:8000/relationship/admin/
- requires librarian role, uses librarian.html ## correct this
http://127.0.0.1:8000/relationship/librarian/
- requires member role, uses member.html ##correct this
http://127.0.0.1:8000/relationship/member/

git rm $(git ls-files --deleted)