from django.contrib import admin
from .models import Exam, ExamResult, MonthlyPerformance

admin.site.register(Exam)
admin.site.register(ExamResult)
admin.site.register(MonthlyPerformance)