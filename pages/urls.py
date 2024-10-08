from django.urls import path

from .views import AboutPageView, ContactPageView, HomePageView, PrivacyPageView

urlpatterns = [
    path("about/", AboutPageView.as_view(), name="about"),
    path("privacy/", PrivacyPageView.as_view(), name="privacy"),
    path("contact/", ContactPageView.as_view(), name="contact"),
    path("", HomePageView.as_view(), name="home"),
]
