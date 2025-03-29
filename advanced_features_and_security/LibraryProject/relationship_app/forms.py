from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    role = forms.ChoiceField(choices=[
        ('Member', 'Member'),
        ('Librarian', 'Librarian'),
        ('Admin', 'Admin')
    ])
    profile_photo = forms.ImageField(required=False)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'role', 'profile_photo', 'password1', 'password2')
        
    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user