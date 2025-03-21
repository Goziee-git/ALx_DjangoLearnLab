from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType
from .models import UserProfile, Book

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        profile = UserProfile.objects.create(user=instance)
        
        # Get content type for Book model
        book_content_type = ContentType.objects.get_for_model(Book)
        
        # Define permission codenames based on role
        if profile.role == 'Admin':
            codenames = ['can_add_book', 'can_change_book', 'can_delete_book', 'can_view_book']
        elif profile.role == 'Librarian':
            codenames = ['can_add_book', 'can_change_book', 'can_view_book']
        else:  # Member
            codenames = ['can_view_book']
            
        # Get and add permissions
        permissions = Permission.objects.filter(
            content_type=book_content_type,
            codename__in=codenames
        )
        instance.user_permissions.add(*permissions)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()