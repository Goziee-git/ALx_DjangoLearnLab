from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import user_passes_test
from .views import views

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
    
    # Authentication URLs - Using Django's built-in class-based views
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(
        template_name='relationship_app/login.html'  # Specify the login template
    ), name='login'),
    path('logout/', LogoutView.as_view(
        template_name='relationship_app/logout.html', next_page='login'  # Specify the logout template
    ), name='logout'),
    
    # Role-based URLs
    path('admin/', user_passes_test(is_admin)(admin_view), name='admin'),
    path('librarian/', user_passes_test(is_librarian)(librarian_view), name='librarian'),
    path('member/', user_passes_test(is_member)(member_view), name='member'),
]