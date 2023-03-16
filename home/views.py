from django.shortcuts import render
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    """Render the homepage"""
    template_name = "index.html"
