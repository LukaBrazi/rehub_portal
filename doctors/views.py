from django.views.generic import TemplateView, ListView


# Create your views here.

class DoctorsPageView(ListView):
    template_name = 'doctors.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'
