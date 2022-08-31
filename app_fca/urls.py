from django.urls import path
from app_fca import views

urlpatterns = [
    path('', views.inicio, name='home'),
    path('altadocente/', views.form_alta_docente, name='altadocente'),
   
]