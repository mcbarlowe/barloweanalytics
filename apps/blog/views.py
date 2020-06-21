# apps/blog/views.py

from django.views.generic import TemplateView


class BlogHomePageView(TemplateView):
    template_name = "blog/blog_home.html"


class AboutView(TemplateView):
    template_name = "blog/about.html"

class HomeView(TemplateView):
    template_name = "home.html"
