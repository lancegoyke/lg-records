"""records_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from records_project.views import favicon

urlpatterns = [
    # Django admin
    path("backside/", admin.site.urls),
    # Authentication (shouldn't need first two no mo')
    # path('accounts/', include('django.contrib.auth.urls')),
    path("accounts/", include("allauth.urls")),
    path("accounts/", include("users.urls")),
    # Local apps
    path("challenges/", include("challenges.urls")),
    path("favicon.ico", favicon),
    path("", include("pages.urls")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    try:
        import debug_toolbar
        urlpatterns = [
            path("__debug__/", include(debug_toolbar.urls)),
        ] + urlpatterns
    except ImportError:
        # Debug toolbar not installed, skip adding debug URLs
        pass
