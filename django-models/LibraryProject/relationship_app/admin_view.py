from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from ..models import Book, Library, UserProfile

def check_admin_role(user):
    """Check if user has Admin role"""
    return user.is_authenticated and user.userprofile.role == 'Admin'

@login_required
@user_passes_test(check_admin_role)
def admin_view(request):
    context = {
        'total_books': Book.objects.count(),
        'total_libraries': Library.objects.count(),
        'total_users': UserProfile.objects.count(),
        'user': request.user
    }
    return render(request, 'relationship_app/admin.html', context)