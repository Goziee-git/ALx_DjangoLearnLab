from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from .models import Book, Library, UserProfile
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import Library

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

# These functions check the role of the user and return True if the user has the specified role.
def is_admin(user):
   return user.userprofile.role == 'Admin'
   
@login_required
@user_passes_test(is_admin)
def Admin(request):
   return render(request, 'relationship_app/admin.html')

def is_librarian(user):
   return user.userprofile.role == 'librarian'

@login_required
@user_passes_test(is_librarian)
def librarian_view(request):
   return render(request, 'relationship_app/librarian.html')

def is_member(user):
   return user.userprofile.role == 'member'

@login_required
@user_passes_test(is_member)
def member_view(request):
   return render(request, 'relationship_app/member.html')

# Define a view for Admin role
@user_passes_test(lambda u: u.is_authenticated and u.userprofile.role == 'Admin')
def admin_view(request):
    # Render the admin view template
    return render(request, 'relationship_app/admin_view.html')

# Define a view for Librarian role
@user_passes_test(lambda u: u.is_authenticated and u.userprofile.role == 'Librarian')
def librarian_view(request):
    # Render the librarian view template
    return render(request, 'relationship_app/librarian_view.html')

# Define a view for Member role
@user_passes_test(lambda u: u.is_authenticated and u.userprofile.role == 'Member')
def member_view(request):
    # Render the member view template
    return render(request, 'relationship_app/member_view.html')
