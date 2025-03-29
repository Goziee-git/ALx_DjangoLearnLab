from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import user_passes_test
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # Main application URLs
    path('books/', views.list_books, name='list_books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
    
    # Authentication URLs - Using Django's built-in class-based views
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'), #uses the as_view method called on the built in LoginView CBV
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html', next_page='login'), name='logout'), #uses the as_view method called on the built in LogoutView CBV
    
    # Role-based URLs
    path('admin/', user_passes_test(views.check_admin_role)(views.admin_view), name='admin'),
    path('librarian/', user_passes_test(views.check_librarian_role)(views.librarian_view), name='librarian'),
    path('member/', user_passes_test(views.check_member_role)(views.member_view), name='member'),

     # Book management URLs
    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/<int:book_id>/', views.edit_book, name='edit_book'),
    path('delete_book/<int:book_id>/', views.delete_book, name='delete_book'),
       
]

#serving the media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)