from django.urls import path

from password_manager import views as password_manager_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', password_manager_views.index, name='index'),
    path('register/', password_manager_views.register_form, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
