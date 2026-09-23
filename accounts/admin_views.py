from django.shortcuts import render

from .decorators import role_required


@role_required(["ADMIN"])
def admin_dashboard(request):
    """
    Main school administrator dashboard.
    """

    context = {
        "page_title": "School Admin Dashboard",
        "user": request.user,
    }

    return render(
        request,
        "accounts/admin_dashboard.html",
        context,
    )