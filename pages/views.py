from django.views.generic import TemplateView, FormView
from django.contrib import messages
from django.urls import reverse_lazy

from .forms import ContactForm


# Create your views here.
class HomePageView(TemplateView):
    template_name = "home.html"


class AboutPageView(TemplateView):
    template_name = "about.html"


class PrivacyPageView(TemplateView):
    template_name = "privacy.html"


class ContactPageView(FormView):
    form_class = ContactForm
    template_name = "contact.html"
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        form.send_email()
        messages.success(self.request, "Contact email sent successfully.")
        return super().form_valid(form)
