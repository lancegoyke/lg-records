from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    template_name = "home.html"


class AboutPageView(TemplateView):
    template_name = 'about.html'


class PrivacyPageView(TemplateView):
    template_name = 'privacy.html'