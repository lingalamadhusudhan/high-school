from django.shortcuts import render
from .decorators import role_required
from students.models import SchoolClass
from homework.models import Homework
from notices.models import Notice


@role_required('TEACHER')
def teacher_dashboard(request):
    my_classes = SchoolClass.objects.filter(class_teacher=request.user)
    my_homework = Homework.objects.filter(school_class__in=my_classes).order_by('-created_at')[:5]
    notices = Notice.objects.filter(school_class__in=my_classes) | Notice.objects.filter(school_class__isnull=True)
    return render(request, 'accounts/teacher_dashboard.html', {
        'my_classes': my_classes,
        'my_homework': my_homework,
        'notices': notices.order_by('-created_at')[:5],
    })