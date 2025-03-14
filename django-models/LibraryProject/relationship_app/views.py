from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from .models import Book, Library, UserProfile
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required, user_passes_test


# This function retrieves all Book objects from the database and renders them in the 'list_books.html' template.
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# This class-based view displays the details of a specific Library object.
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

# This function handles user registration. It processes the form data, creates a new user, logs them in, and redirects to the list_books view.
def register(request):
   if request.method == 'POST':
      form = UserCreationForm(request.POST)
      if form.is_valid():
         user = form.save()
         login(request, user)
         return redirect('list_books')
   else:
      form = UserCreationForm()
   return render(request, 'relationship_app/register.html', {'form': form})

# This function handles user login. It processes the form data, authenticates the user, logs them in, and redirects to the list_books view.
def user_login(request):
   if request.method == 'POST':
      form = AuthenticationForm(request, data=request.POST)
      if form.is_valid():
         user = form.get_user()
         login(request, user)
         return redirect('list_books')
   else:
      form = AuthenticationForm()
   return render(request, 'relationship_app/login.html', {'form': form})

# This function logs out the user and renders the 'logout.html' template.
'''
this code below is formatted because it tries to use the GET request for the logout operation and is not
recommended for security reasons
'''
#def user_logout(request):
#    logout(request)
#   return render(request, 'relationship_app/logout.html')


