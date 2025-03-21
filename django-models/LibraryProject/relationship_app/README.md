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

>>> Common Web Vulnerabilities and their Impact

- Cross-Site Scripting (XSS): Attackers inject malicious scripts into web pages viewed by users. These scripts can steal sensitive data like cookies or login credentials, deface websites, or redirect users to phishing sites.
- Cross-Site Request Forgery (CSRF): Malicious actors trick users into performing actions on a trusted website without their knowledge or consent. This can lead to unauthorized fund transfers, data modification, or account takeover.
- SQL Injection: Attackers manipulate database queries to gain unauthorized access to sensitive data, modify data, or even delete entire databases. This can have severe consequences, including data breaches and financial losses.
- Clickjacking: Users are deceived into clicking seemingly innocuous elements on a web page, while hidden elements perform unintended actions in the background. This can lead to the installation of malware, unauthorized purchases, or social media hijacking.

>>> Leveraging Django’s Built-in Security Features
Django comes equipped with several built-in security features designed to mitigate these vulnerabilities:

- CSRF Protection: Django’s CSRF middleware automatically generates and validates tokens for forms. This ensures that only forms originating from your own website can submit data, preventing CSRF attacks.
- XSS Protection: Django templates automatically escape user-provided data by default. This process converts special characters into harmless entities, preventing malicious scripts from being executed in the browser.
- SQL Injection Protection: Django’s querysets and ORM (Object-Relational Mapper) provide a secure way to interact with databases. They use parameterization to ensure that user input is treated as data, not executable code, preventing SQL injection attacks.
- Password Hashing: Django stores passwords securely using robust hashing algorithms like PBKDF2 or Argon2. This makes it extremely difficult for attackers to crack passwords even if they gain access to the hashed password data.
>>> Implementing Secure Development Practices
While Django provides a strong foundation for security, adopting secure development practices is essential to build truly resilient applications:

- Validate User Input: Always validate and sanitize user input to prevent malicious data from entering your application. This involves checking for data type, length, format, and allowed characters.
- Use Parameterized Queries: Avoid using raw SQL queries that concatenate user input directly into the query string. Instead, use Django’s ORM or parameterized queries, which separate data from code and prevent SQL injection.
- Keep Dependencies Updated: Regularly update Django, its dependencies, and any third-party libraries you use in your application. This ensures you benefit from the latest security patches and bug fixes.
- Implement Strong Authentication: Enforce strong password policies that require users to create complex passwords with a mix of characters. Consider implementing multi-factor authentication for an extra layer of security.
- Use HTTPS: Implement HTTPS to encrypt communication between the client and server. This protects sensitive data transmitted over the network, such as login credentials and financial information, from eavesdropping and man-in-the-middle attacks.
- Principle of Least Privilege: Grant users the minimum level of access necessary to perform their tasks. This limits the potential damage in case of a compromised account.