from django.urls import path

from .views import ChallengeListView, ChallengeDetailView

urlpatterns = [
    path('', ChallengeListView.as_view(), name="challenge_list"),
    path('<str:slug>', ChallengeDetailView.as_view(), name="challenge_detail"),
]