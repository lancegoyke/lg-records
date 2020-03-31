from django.http import HttpResponseForbidden
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, FormView
)
from django.views.generic.detail import SingleObjectMixin
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import (
    LoginRequiredMixin, PermissionRequiredMixin
)
from django.db.models import Q

from .filters import ChallengeFilter, RecordFilter
from .models import Challenge, Record
from .forms import RecordCreateForm

# Create your views here.
@login_required()
def challenge_filtered_list(request):
    filter = ChallengeFilter(request.GET, queryset=Challenge.objects.all().order_by('-date_created'))
    return render(request, 'challenges/challenge_filtered_list.html', {'filter': filter})


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


class ChallengeDisplay(DetailView):
    model = Challenge

    # make sure the RecordCreateForm is available in the template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['record_create_form'] = RecordCreateForm()
        context['filter'] = RecordFilter(self.request.GET, queryset=self.get_object().records.order_by('-date_recorded'))
        return context


class RecordCreate(SingleObjectMixin, FormView):
    template_name = 'challenges/challenge_detail.html'
    form_class = RecordCreateForm # FormView
    model = Challenge # SingleObjectMixin

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    # redirect to challenge_detail page after adding new record
    def get_success_url(self):
        return reverse('challenge_detail', kwargs={'slug': self.object.slug})

    def form_valid(self, form):
        # assign current user to the score being recorded
        form.instance.user = self.request.user
        # assign current challenge from SingleObjectMixin to score being
        # recorded
        form.instance.challenge = self.get_object()
        # don't forget to save!
        form.save()
        return super(RecordCreate, self).form_valid(form)


class ChallengeDetail(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        view = ChallengeDisplay.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = RecordCreate.as_view()
        return view(request, *args, **kwargs)