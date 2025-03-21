# this signals file here is used by django UserProfile models to automatically create a UserProfile for each user that is created.
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserProfile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

        #here i assign permissions based on role
        if profile.role == 'Admin':
            permissions = ['can_add_book', 'can_edit_book', 'can_delete_book',
            'can_view_book']
        elif profile.role == 'Librarian':
            permissions = ['can_add_book', 'can_edit_book', 'can_view_book']
        else:
            permissions = ['can_view_book']

        for perm in permissions:
            instance.user_permissions.add(f'relationship_app.{perm}')


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()