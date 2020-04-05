from django.urls import reverse_lazy
from django.views import generic

from .models import CustomUser
from .forms import CustomUserChangeForm

# Create your views here.
# class CustomUserDetailView(generic.DetailView):
#     model = CustomUser
#     template_name = 'account/user_detail.html'



class CustomUserDetailView(generic.TemplateView):
    template_name = 'account/user_detail.html'

    

class CustomUserUpdateView(generic.UpdateView):
    model = CustomUser
    form_class = CustomUserChangeForm
    template_name = 'account/user_update.html'