from django.contrib import admin
from home.models import User, Booking, Mentor, Woman


admin.site.register(User)


@admin.register(Mentor)
class MentorAdmin(admin.ModelAdmin):
    list_display = ('username', 'email')


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('mentor', 'user', 'date', 'time')
