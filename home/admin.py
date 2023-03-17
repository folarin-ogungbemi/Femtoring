from django.contrib import admin
from home.models import User, Booking


admin.site.register(User)


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('mentor', 'user', 'date', 'time')
