from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic import TemplateView, ListView, DetailView
from django.views import generic, View
from home.models import MentorsProfile, Mentor, User
from home.forms import BookingForm
from django.contrib import messages


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
            messages.success(request, 'Your booking was successful.')
            return redirect(reverse('home_page'))
        elif form.errors:
            messages.error(request, 'There was a problem submitting the form.')
        return render(request, "booking.html", {"mentor": mentor, "form": form})
