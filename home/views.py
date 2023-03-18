from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import FormView
from django.views import generic, View
from home.models import MentorsProfile, Mentor, User
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

        mentor_profile = get_object_or_404(MentorsProfile, pk=pk)

        return render(request, "profile.html", {"mentor_profile": mentor_profile})


class BookingView(View):

    def get(self, request, pk=None):

        mentor = get_object_or_404(MentorsProfile, pk=pk)

        form = BookingForm()

        return render(request, "booking.html", {"mentor": mentor, "form": form})

    def post(self, request, pk=None):

        mentor = get_object_or_404(MentorsProfile, pk=pk)

        form = BookingForm(data=request.POST)
        if form.is_valid():
            form.instance.user = request.user
            booking = form.save(commit=False)
            booking.mentor = mentor.mentor_name
            booking.save()
            return redirect(reverse('home_page'))
        return render(request, "booking.html", {"mentor": mentor, "form": form})
