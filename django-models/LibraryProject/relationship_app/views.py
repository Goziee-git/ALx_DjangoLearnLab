from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.detail import DetailView
from .models import Book, Library, UserProfile
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from django.http import HttpResponseForbidden
from .utils import assign_admin_permissions, assign_librarian_permissions, assign_member_permissions


# This function retrieves all Book objects from the database and renders them in the 'list_books.html' template.
@login_required
@permission_required('relationship_app.can_view_book', raise_exception=True)
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books, 'error': None})

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
         #Assigning role-based permissions
         if user.userprofile.role == 'Admin':
            assign_admin_permissions(user)
         elif user.userprofile.role == 'Member':
            assign_member_permissions(user)
         elif user.userprofile.role == 'Librarian':
            assign_librarian_permissions(user)
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

@login_required
@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author_id = request.POST.get('author')
        if title and author_id:
            Book.objects.create(
                title=title,
                author_id=author_id
            )
            return redirect('list_books')
        else:
            return render(request, 'relationship_app/add_book.html', {'error': 'Title and Author are required.'})
    return render(request, 'relationship_app/add_book.html', {'error': None})

@login_required
@permission_required('relationship_app.can_edit_book', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        title = request.POST.get('title')
        author_id = request.POST.get('author')
        if title and author_id:
            book.title = title
            book.author_id = author_id
            book.save()
            return redirect('list_books')
        else:
            return render(request, 'relationship_app/edit_book.html', {'book': book, 'error': 'Title and Author are required.'})
    return render(request, 'relationship_app/edit_book.html', {'book': book, 'error': None})

        

@login_required
@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('list_books')
    return render(request, 'relationship_app/delete_book.html', {'book': book, 'error': 'Are you sure you want to delete this book?'})





def check_librarian_role(user):
    """Check if user has Librarian role"""
    return user.is_authenticated and user.userprofile.role == 'Librarian'

@login_required
@user_passes_test(check_librarian_role)
def librarian_view(request):
    context = {
        'books': Book.objects.all(),
        'libraries': Library.objects.all(),
    }
    return render(request, 'relationship_app/librarian.html', context)


def check_member_role(user):
    """Check if user has Member role"""
    return user.is_authenticated and user.userprofile.role == 'Member'

@login_required
@user_passes_test(check_member_role)
def member_view(request):
    return render(request, 'relationship_app/member.html')

def check_admin_role(user):
    """Check if user has Admin role"""
    return user.is_authenticated and user.userprofile.role == 'Admin'

@login_required
@user_passes_test(check_admin_role)
def admin_view(request):
    user = request.user
    if not user.has_perm('relationship_app.can_add_book'):
        user.user_permissions.add('relationship_app.can_add_book')
        user.user_permissions.add('relationship_app.can_edit_book')
        user.user_permissions.add('relationship_app.can_delete_book')
        user.user_permissions.add('relationship_app.can_view_book')
    context = {
        'total_books': Book.objects.count(),
        'total_libraries': Library.objects.count(),
        'total_users': UserProfile.objects.count(),
        'user': request.user
    }
    return render(request, 'relationship_app/admin.html', context)
