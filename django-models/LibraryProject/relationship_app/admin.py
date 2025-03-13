from django.contrib import admin
from .models import Author, Book, Library, Librarian, UserProfile

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Library)
admin.site.register(Librarian)

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
   list_display = ('user', 'role')  # Show user and role in the admin panel
   list_filter = ('role',)  # Filter by role in the admin panel