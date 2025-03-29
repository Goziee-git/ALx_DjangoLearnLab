from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import CustomUser, Book

User = get_user_model()

@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    """Create a UserProfile when a new user is created"""
    if created:
        if not instance.role:
            instance.role = "Member"
            instance.save()
        print(f"NEW USER CREATED: {instance.username} with role {instance.role}")

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    """perform additional actions when a CustomUser is saved"""
    if instance.profile_photo and not instance.profile_photo.name.endswith(('.jpg','.png')):
        print(f"invalid profile photo format for user {instance.username}")