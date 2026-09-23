from django.urls import path
from . import teacher_views

urlpatterns = [
    path('', teacher_views.teacher_dashboard, name='teacher_dashboard'),
]