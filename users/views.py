from django.views import generic

from .forms import CustomUserChangeForm
from .models import CustomUser


class CustomUserDetailView(generic.TemplateView):
    template_name = "account/user_detail.html"


class CustomUserUpdateView(generic.UpdateView):
    model = CustomUser
    form_class = CustomUserChangeForm
    template_name = "account/user_update.html"
