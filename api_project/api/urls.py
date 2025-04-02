from django.urls import path, include
from .views import BookList, BookViewSet
from rest_framework.routers import DefaultRouter

#a router and register for BookViewSet
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
   #route for the BookList view
    path('books/', BookList.as_view(), name='book-list'),

    #Include the router URLs for BookViewSet
    path('', include(router.urls)),
]
