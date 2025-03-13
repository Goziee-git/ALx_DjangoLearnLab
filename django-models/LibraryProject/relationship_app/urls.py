from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import user_passes_test
from . import views

def is_admin(user):
    return user.is_authenticated and user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.is_authenticated and user.userprofile.role == 'Librarian'

def is_member(user):
    return user.is_authenticated and user.userprofile.role == 'Member'

urlpatterns = [
    # Main application URLs
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    
    # Authentication URLs - Using Django's built-in class-based views
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'), #uses the as_view method called on the built in LoginView CBV
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html', next_page='login'), name='logout'), #uses the as_view method called on the built in LogoutView CBV
    
    # Role-based URLs
    path('admin/', user_passes_test(is_admin)(views.admin_view), name='admin'),
    path('librarian/', user_passes_test(is_librarian)(views.librarian_view), name='librarian'),
    path('member/', user_passes_test(is_member)(views.member_view), name='member'),
]