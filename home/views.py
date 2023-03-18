from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView
from home.models import MentorsProfile, Mentor
from home.forms import BookingForm


class HomePageView(TemplateView):
    """Render the homepage"""
    template_name = "index.html"


class AboutView(TemplateView):
    """Render the About us view page"""
    template_name = "about.html"


class MentorsList(ListView):
    """Render the Mentors page"""
    model = MentorsProfile
    template_name = "mentors.html"
    paginate_by = 6


class MentorDetail(DetailView):

    def get(self, request, pk=None):
        if pk:

            mentor_profile = get_object_or_404(MentorsProfile, pk=pk)
        else:
            mentor_profile = request.mentor_id

        return render(request, "profile.html", {"mentor_profile": mentor_profile})


class BookingView(TemplateView):
    template_name = "booking.html"