from django.urls import path

from .views import ChallengeListView, ChallengeDetailView, SearchResultsListView

urlpatterns = [
    path('', ChallengeListView.as_view(), name="challenge_list"),
    path('<str:slug>', ChallengeDetailView.as_view(), name="challenge_detail"),
    path('search/', SearchResultsListView.as_view(), name="search_results"),
]