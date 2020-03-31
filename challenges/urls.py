from django.urls import path

from .models import Challenge
from .views import (
    ChallengeCreateView, 
    ChallengeUpdateView,
    ChallengeDetail,
    challenge_filtered_list,
)

urlpatterns = [
    path('<str:slug>/update/', ChallengeUpdateView.as_view(), name="challenge_update"),
    path('<str:slug>', ChallengeDetail.as_view(), name="challenge_detail"),
    path('new/', ChallengeCreateView.as_view(), name="challenge_create"),
    path('', challenge_filtered_list, name='challenge_filtered_list'),
]