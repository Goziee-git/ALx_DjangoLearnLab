from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from .models import Book

def get_book_permissions():
    """Get all book-related permissions"""
    return Permission.objects.filter(
        content_type=ContentType.objects.get_for_model(Book)
    )

def assign_admin_permissions(user):
    """Assign all book permissions to admin users"""
    book_permissions = get_book_permissions()
    user.user_permissions.add(*book_permissions)
    user.save()

def assign_librarian_permissions(user):
    """Assign view, add, and edit permissions to librarian users"""
    book_permissions = Permission.objects.filter(
        content_type=ContentType.objects.get_for_model(Book),
        codename__in=['can_view_book', 'can_add_book', 'can_edit_book']
    )
    user.user_permissions.add(*book_permissions)
    user.save()

def assign_member_permissions(user):
    """Assign view-only permissions to member users"""
    view_permission = Permission.objects.get(
        content_type=ContentType.objects.get_for_model(Book),
        codename='can_view_book'
    )
    user.user_permissions.add(view_permission)
    user.save()