from django import forms
from django.core.mail import send_mail


class ContactForm(forms.Form):
    email = forms.EmailField(
        widget=forms.TextInput(attrs={"class": "special"}), required=True
    )
    message = forms.CharField(max_length=1000, widget=forms.Textarea, required=True)

    def send_email(self):
        email_subject = "[lg-records] Contact Form"
        email_message = self.cleaned_data["message"]
        email_from = self.cleaned_data["email"]
        email_to = ("lance@lancegoyke.com",)
        return send_mail(
            email_subject, email_message, email_from, email_to, fail_silently=False
        )
