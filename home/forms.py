from django.forms import ModelForm
from home.models import Booking


class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = ['user', 'mentor', 'date', 'date', 'time', 'message']