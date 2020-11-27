from django.urls import path
from . import views

urlpatterns = [
    path('doctors', views.DoctorViews.as_view(), name='our_doctors')
]
