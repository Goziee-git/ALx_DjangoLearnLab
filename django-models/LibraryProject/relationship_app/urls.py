from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import user_passes_test
from . import views 
from . view.admin_view import check_admin_role, admin_view
from . view.librarian_view import check_librarian_role, librarian_view
from . view.member_view import check_member_role, member_view


urlpatterns = [
    # Main application URLs
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    
    # Authentication URLs - Using Django's built-in class-based views
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'), #uses the as_view method called on the built in LoginView CBV
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html', next_page='login'), name='logout'), #uses the as_view method called on the built in LogoutView CBV
    
    # Role-based URLs
    path('admin/', user_passes_test(check_admin_role)(admin_view), name='admin'),
    path('librarian/', user_passes_test(check_librarian_role)(librarian_view), name='librarian'),
    path('member/', user_passes_test(check_member_role)(member_view), name='member'),
]