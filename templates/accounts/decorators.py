from functools import wraps
from django.shortcuts import redirect
from django.core.exceptions import PermissionDenied

def role_required(allowed_roles):
    """
    Decorator to check user role.
    Redirects unauthenticated users to the login page (302).
    Raises PermissionDenied (403) for authenticated users with insufficient permissions.
    """
    if isinstance(allowed_roles, str):
        allowed_roles = [allowed_roles]

    def decorator(view_func):
        @wraps(view_func)
        def wrapper(request, *args, **kwargs):
            if not request.user.is_authenticated:
                return redirect('login')
            
            # Check user role (adjust attribute if your model uses e.g. request.user.role)
            user_role = getattr(request.user, 'role', None)
            if user_role not in allowed_roles and not request.user.is_superuser:
                raise PermissionDenied

            return view_func(request, *args, **kwargs)
        return wrapper
    return decorator