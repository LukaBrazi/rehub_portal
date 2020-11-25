from django.urls import path
from . import views


urlpatterns = [
    path('', views.DoctorsPageView.as_view(), name='doctors'),
    path('about', views.AboutPageView.as_view(), name='about'),
    path('doctors/new/', views.CreateDoctorView.as_view(), name='new_doc'),
    ]
