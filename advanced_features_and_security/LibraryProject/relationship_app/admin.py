from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Author, Book, Library, Librarian, CustomUser

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Library)
admin.site.register(Librarian)

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
  fieldsets = UserAdmin.fieldsets + (
   (None, {'fields': ('date_of_birth', 'profile_photo')}),
  )
  add_fieldsets = UserAdmin.add_fieldsets +  (
   (None, {'fields': ('date_of_birth', 'profile_photo')})
  )