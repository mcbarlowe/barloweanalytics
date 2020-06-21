# barloweanalytics/urls.py

from django.contrib import admin
from django.urls import path, include
from apps.blog.views import HomeView

urlpatterns = [
    # Django admin
    path("admin/", admin.site.urls),
    # User management
    path("accounts/", include("allauth.urls")),
    # Local apps
    # blog urls
    path("blog/", include("apps.blog.urls")),
    # home page
    path("", HomeView.as_view(), name="home")
]
