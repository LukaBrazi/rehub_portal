from django.shortcuts import render

# Create your views here.
from django.views import View

from .models import Doctor


class DoctorViews(View):

    def get(self, request):
        doctors = Doctor.objects.all()
        return render(request, 'doctors/doctor_list.html', context={'doctor_list': doctors})
