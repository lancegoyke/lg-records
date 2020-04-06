from django.urls import path

from .views import HomePageView, AboutPageView, PrivacyPageView

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('privacy/', PrivacyPageView.as_view(), name='privacy'),
    path('', HomePageView.as_view(), name='home'),
]