from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import register, list_books, LibraryDetailView, user_login, user_logout, Admin, librarian_view, member_view

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('admin/', Admin, name='admin'),
    path('librarian/', librarian_view, name='librarian'),
    path('member/', member_view, name='member'),
]