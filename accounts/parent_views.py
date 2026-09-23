from django.shortcuts import render
from .decorators import role_required
from students.models import Student


@role_required('PARENT')
def parent_dashboard(request):
    my_children = Student.objects.filter(parent=request.user)
    return render(request, 'accounts/parent_dashboard.html', {'my_children': my_children})