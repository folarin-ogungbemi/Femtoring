from django.contrib import admin
from django.urls import path
from home import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home_page'),
    path('mentors/', views.MentorsList.as_view(), name='mentors_page'),
    path('about/', views.AboutView.as_view(), name='about_us_page'),
    path(
        'mentors/<slug:slug>/',
        views.MentorDetail.as_view(), name="mentor_profile_page"),
    path(
        'mentors/booking/<slug:slug>/', login_required(
            views.BookingView.as_view()), name='booking_page'),
]
