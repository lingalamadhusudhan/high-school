from functools import wraps

from django.contrib.auth.views import redirect_to_login
from django.core.exceptions import PermissionDenied


def role_required(allowed_roles):
    """
    Restrict a view to one or more user roles.

    Logged-out user:
        Redirect to login page.

    Logged-in user with incorrect role:
        Return 403 Forbidden.

    Logged-in user with correct role:
        Allow access.
    """

    def decorator(view_func):

        @wraps(view_func)
        def wrapper(request, *args, **kwargs):

            # --------------------------------------------
            # User must first be authenticated
            # --------------------------------------------

            if not request.user.is_authenticated:
                return redirect_to_login(
                    request.get_full_path()
                )

            # --------------------------------------------
            # Get user's role safely
            # --------------------------------------------

            user_role = getattr(
                request.user,
                "role",
                None,
            )

            # --------------------------------------------
            # Check authorization
            # --------------------------------------------

            if user_role not in allowed_roles:
                raise PermissionDenied

            # --------------------------------------------
            # Authorized
            # --------------------------------------------

            return view_func(
                request,
                *args,
                **kwargs
            )

        return wrapper

    return decorator