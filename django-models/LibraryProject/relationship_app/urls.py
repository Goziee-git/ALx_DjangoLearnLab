from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from relationship_app.views.register import register
from relationship_app.views.list_books import list_books
from relationship_app.views.library_detail_view import LibraryDetailView
from relationship_app.views.user_login import user_login
from relationship_app.views.user_logout import user_logout
from relationship_app.views.admin_view import admin_view
from relationship_app.views.librarian_view import librarian_view
from relationship_app.views.member_view import member_view

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('admin/', admin_view, name='admin'),
    path('librarian/', librarian_view, name='librarian'),
    path('member/', member_view, name='member'),
]