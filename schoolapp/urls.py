from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from accounts import views as account_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('dashboard/', account_views.dashboard_redirect, name='dashboard'),
    path('admin-panel/', include('accounts.admin_urls')),
    path('teacher/', include('accounts.teacher_urls')),
    path('parent/', include('accounts.parent_urls')),
]
