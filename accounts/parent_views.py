from django.shortcuts import render
from .decorators import role_required
from students.models import Student
from attendance.models import AttendanceRecord
from homework.models import Homework
from exams.models import ExamResult, MonthlyPerformance
from notices.models import Notice


@role_required('PARENT')
def parent_dashboard(request):
    my_children = Student.objects.filter(parent=request.user)
    context = {'my_children': my_children, 'children_data': []}

    for child in my_children:
        context['children_data'].append({
            'student': child,
            'attendance': AttendanceRecord.objects.filter(student=child).order_by('-date')[:10],
            'homework': Homework.objects.filter(school_class=child.school_class).order_by('-created_at')[:5],
            'results': ExamResult.objects.filter(student=child).order_by('-id')[:10],
            'performance': MonthlyPerformance.objects.filter(student=child).order_by('-month')[:6],
        })
    return render(request, 'accounts/parent_dashboard.html', context)