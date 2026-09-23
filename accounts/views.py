from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect


@login_required
def dashboard_redirect(request):
    role = request.user.role
    if role == 'ADMIN':
        return redirect('admin_dashboard')
    elif role == 'TEACHER':
        return redirect('teacher_dashboard')
    elif role == 'PARENT':
        return redirect('parent_dashboard')
    return redirect('login')