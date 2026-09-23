from django.urls import path
from . import parent_views

urlpatterns = [
    path('', parent_views.parent_dashboard, name='parent_dashboard'),
]