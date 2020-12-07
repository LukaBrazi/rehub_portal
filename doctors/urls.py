from django.urls import path
from . import views

urlpatterns = [
    path('doctors', views.DoctorViews.as_view(), name='our_doctors'),
    path('<int:pk>', views.DoctorDetailViews.as_view(), name='doctor_detail'),
    path('review/<int:pk>', views.AddReview.as_view(), name='add_review')
]
