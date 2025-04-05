from django.urls import path

from password_manager import views

urlpatterns = [
    path('', views.index, name='index'),
    path('template-index/', views.template_index, name='template_index'),
]
