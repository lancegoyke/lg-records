from django.views.generic import ListView, DetailView

from .models import Challenge

# Create your views here.
class ChallengeListView(ListView):
    model = Challenge
    context_object_name = 'challenges'
    template_name = 'challenges/challenge_list.html'


class ChallengeDetailView(DetailView):
    model = Challenge
    context_object_name = 'challenge'
    template_name = 'challenges/challenge_detail.html'