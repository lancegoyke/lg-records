from django.urls import path

from .views import (
    ChallengeListView, ChallengeDetailView, SearchResultsListView,
    ChallengeCreateView, ChallengeUpdateView
)

urlpatterns = [
    path('<str:slug>', ChallengeDetailView.as_view(), name="challenge_detail"),
    path('<str:slug>/update/', ChallengeUpdateView.as_view(), name="challenge_update"),
    path('new/', ChallengeCreateView.as_view(), name="challenge_create"),
    path('search', SearchResultsListView.as_view(), name="search_results"),
    path('', ChallengeListView.as_view(), name="challenge_list"),
]