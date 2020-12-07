from django.shortcuts import render, redirect

# Create your views here.
from django.views import View
from .forms import ReviewForm
from .models import Doctor


class DoctorViews(View):

    def get(self, request):
        doctors = Doctor.objects.all()
        return render(request, 'doctors/doctor_list.html', context={'doctor_list': doctors})


class DoctorDetailViews(View):

    def get(self, request, pk):
        doctor = Doctor.objects.get(id=pk)
        return render(request, 'doctors/doctor_detail.html', context={'doctor_detail': doctor})


class AddReview(View):

    def post(self, request, pk):
        doctor = Doctor.objects.get(id=pk)
        form = ReviewForm(request.POST)
        current_user = request.user
        if form.is_valid():
            form = form.save(commit=False)
            form.doctor_id = doctor.pk
            form.user_id = current_user.id
            form.save()
        return redirect(doctor.get_absolute_url())
