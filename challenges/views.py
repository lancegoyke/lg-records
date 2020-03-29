from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView
)
from django.contrib.auth.mixins import (
    LoginRequiredMixin, PermissionRequiredMixin
)
from django.db.models import Q
from django.contrib import messages

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


class SearchResultsListView(LoginRequiredMixin, ListView):
    model = Challenge
    context_object_name = 'challenges'
    template_name = 'challenges/search_results.html'


    def get_queryset(self):
        query = self.request.GET.get('q')
        return Challenge.objects.filter(
            Q(name__icontains=query) | Q(name__icontains=query)
        )


class ChallengeCreateView(PermissionRequiredMixin, CreateView):
    model = Challenge
    template_name = "challenges/challenge_create.html"
    fields = ['name', 'description', 'tags',]
    permission_required = ('challenges.can_edit',)
    raise_exception = False

    def handle_no_permission(self):
        messages.error(self.request, "You don't have permission to create a challenge.")
        return super(ChallengeCreateView, self).handle_no_permission()


class ChallengeUpdateView(PermissionRequiredMixin, UpdateView):
    model = Challenge
    template_name = "challenges/challenge_update.html"
    fields = ['name', 'description', 'tags',]
    permission_required = ('challenges.can_edit',)
    raise_exception = False
    login_url = 'account_login'

    def handle_no_permission(self):
        messages.error(self.request, "You don't have permission to update a challenge.")
        return super(ChallengeUpdateView, self).handle_no_permission()