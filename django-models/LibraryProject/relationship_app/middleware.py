from django.http import HttpResponseForbidden
from django.utils.deprecation import MiddlewareMixin

class PermissionMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # Check if the user is authenticated
        if request.user.is_authenticated:
            # Check for specific permissions based on the request path
            if request.path.startswith('/add_book/') and not request.user.has_perm('relationship_app.can_add_book'):
                return HttpResponseForbidden("You do not have permission to add books.")
            elif request.path.startswith('/change_book/') and not request.user.has_perm('relationship_app.can_edit_book'):
                return HttpResponseForbidden("You do not have permission to edit books.")
            elif request.path.startswith('/delete_book/') and not request.user.has_perm('relationship_app.can_delete_book'):
                return HttpResponseForbidden("You do not have permission to delete books.")
        return None


#I will now proceed to implement the middleware for additional security, which will check user permissions for all incoming requests. This will help enforce URL-based access control.