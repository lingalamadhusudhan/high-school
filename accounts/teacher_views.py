from django.shortcuts import render
from .decorators import role_required
from students.models import SchoolClass


@role_required('TEACHER')
def teacher_dashboard(request):
    my_classes = SchoolClass.objects.filter(class_teacher=request.user)
    return render(request, 'accounts/teacher_dashboard.html', {'my_classes': my_classes})