from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import user_passes_test
from .views import (
    register,  # Explicitly import register view
    list_books, 
    LibraryDetailView, 
    user_login, 
    user_logout, 
    admin_view, 
    librarian_view, 
    member_view
)

def is_admin(user):
    return user.is_authenticated and user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.is_authenticated and user.userprofile.role == 'Librarian'

def is_member(user):
    return user.is_authenticated and user.userprofile.role == 'Member'

urlpatterns = [
    # Main application URLs
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    
    # Authentication URLs
    path('register/', register, name='register'),  # Register URL should match views.register
    path('accounts/login/', user_login, name='login'),
    path('accounts/logout/', user_logout, name='logout'),
    
    # Role-based URLs
    path('admin/', user_passes_test(is_admin)(admin_view), name='admin'),
    path('librarian/', user_passes_test(is_librarian)(librarian_view), name='librarian'),
    path('member/', user_passes_test(is_member)(member_view), name='member'),
]