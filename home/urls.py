from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home_page'),
    path('mentors/', views.MentorsView.as_view(), name='mentors_page'),
    path('about/', views.AboutView.as_view(), name='about_us_page'),
]
