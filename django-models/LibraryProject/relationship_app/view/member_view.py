from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test

def check_member_role(user):
    """Check if user has Member role"""
    return user.is_authenticated and user.userprofile.role == 'Member'

@login_required
@user_passes_test(check_member_role)
def member_view(request):
    return render(request, 'relationship_app/member.html')