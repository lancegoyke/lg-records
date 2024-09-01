from django.urls import path

from .views import CustomUserDetailView, CustomUserUpdateView

urlpatterns = [
    path("<uuid:pk>/update", CustomUserUpdateView.as_view(), name="user_update"),
    path("", CustomUserDetailView.as_view(), name="user_detail"),
]
