from django.shortcuts import render
from django.views.generic import TemplateView, ListView


class HomePageView(TemplateView):
    """Render the homepage"""
    template_name = "index.html"


class AboutView(TemplateView):
    """Render the About us view page"""
    template_name = "about.html"


class MentorsView(TemplateView):
    """Render the Mentors page"""
    template_name = "mentors.html"
