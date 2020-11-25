from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView

from .models import Doctor


class DoctorsPageView(ListView):
    model = Doctor
    context_object_name = 'Doctor'
    template_name = 'doctors.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'


class CreateDoctorView(CreateView):
    model = Doctor
    fields = ['first_name',
              'second_name',
              'bio',
              'email',
              'profession'
              ]
    template_name = 'new_doc.html'
