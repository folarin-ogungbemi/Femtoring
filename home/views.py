from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.views.generic import TemplateView, ListView, DetailView, View
from home.models import MentorsProfile, Mentor, User, Booking
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
    context_object_name = "mentors"
    paginate_by = 6


class MentorDetail(DetailView):
    model = Mentor
    template_name = 'profile.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mentor_profile = self.object.mentor_profile
        print(mentor_profile)
        context['mentor_name'] = mentor_profile.mentor_name
        context['mentor_image'] = mentor_profile.mentor_image
        context['mentor_expertise'] = mentor_profile.mentor_expertise
        context['mentor_about'] = mentor_profile.mentor_about
        context['mentor_years_of_experience'] = (
            mentor_profile.mentor_years_of_experience)
        context['messages'] = Booking.objects.filter(mentor=self.object)
        return context


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
        return render(request, {"mentor": mentor, "form": form})


class MentorMessageListView(ListView):
    """
    Mentor Read messages from Users
    """
    model = Booking
    form_class = BookingForm
    template_name = 'profile.html'
    context_object_name = 'messages'
    paginate_by = 5

    def get_queryset(self):
        return Booking.objects.filter(client=self.request.user.id)
