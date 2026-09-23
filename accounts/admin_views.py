from django.shortcuts import render
from .decorators import role_required


@role_required('ADMIN')
def admin_dashboard(request):
    return render(request, 'accounts/admin_dashboard.html')