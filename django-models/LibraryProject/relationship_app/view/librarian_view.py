from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from ..models import Book, Library

def check_librarian_role(user):
    """Check if user has Librarian role"""
    return user.is_authenticated and user.userprofile.role == 'Librarian'

@login_required
@user_passes_test(check_librarian_role)
def librarian_view(request):
    context = {
        'books': Book.objects.all(),
        'libraries': Library.objects.all(),
    }
    return render(request, 'relationship_app/librarian.html', context)