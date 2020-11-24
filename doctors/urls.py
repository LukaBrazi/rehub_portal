from django.urls import path
from . import views


urlpatterns = [
    path('doctors', views.DoctorsPageView.as_view(), name='doctors'),
    path('about', views.AboutPageView.as_view(), name='about'),
    ]
