from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q

from .models import Challenge

# Create your views here.
class ChallengeListView(LoginRequiredMixin, ListView):
    model = Challenge
    context_object_name = 'challenges'
    template_name = 'challenges/challenge_list.html'
    login_url = 'account_login'


class ChallengeDetailView(LoginRequiredMixin, DetailView):
    model = Challenge
    context_object_name = 'challenge'
    template_name = 'challenges/challenge_detail.html'
    login_url = 'account_login'


class SearchResultsListView(ListView):
    model = Challenge
    context_object_name = 'challenges'
    template_name = 'challenges/search_results.html'


    def get_queryset(self):
        query = self.request.GET.get('q')
        return Challenge.objects.filter(
            Q(name__icontains=query) | Q(name__icontains=query)
        )