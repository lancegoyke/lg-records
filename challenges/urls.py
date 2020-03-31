from django.urls import path

from .models import Challenge
from .views import (
    # ChallengeDetailView,
    ChallengeListView, 
    SearchResultsListView,
    ChallengeCreateView, 
    ChallengeUpdateView,
    ChallengeDetail,
    challenge_filtered_list,
)

urlpatterns = [
    # path('<str:slug>/new/', RecordCreateView.as_view(), name="record_create"),
    path('<str:slug>/update/', ChallengeUpdateView.as_view(), name="challenge_update"),
    # path('<str:slug>', ChallengeDetailView.as_view(), name="challenge_detail"),
    path('<str:slug>', ChallengeDetail.as_view(), name="challenge_detail"),
    path('new/', ChallengeCreateView.as_view(), name="challenge_create"),
    path('search', SearchResultsListView.as_view(), name="search_results"),
    path('', challenge_filtered_list, name='challenge_filtered_list'),
    path('', ChallengeListView.as_view(), name="challenge_list"),
]