# apps/blog/urls.py

from django.urls import path

from .views import BlogHomePageView, AboutView

app_name = "blog"

urlpatterns = [
    path("", BlogHomePageView.as_view(), name="blog_home"),
    path("about/", AboutView.as_view(), name="about"),
]
