
from django.db import models

# Create your models here.
class Book(models.Model):
   title = models.CharField(max_length=200)
   author = models.CharField(max_length=100)
   publication_year = models.IntegerField()

   def __str__(self):
      return self.title

      
class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='Member')

    objects = CustomUserManager()  # Attach the custom manager

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'custom_user'
        verbose_name = 'Custom User'
        verbose_name_plural = 'Custom Users'