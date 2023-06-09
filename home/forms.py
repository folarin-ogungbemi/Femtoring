from django import forms
from allauth.account.forms import SignupForm
from home.models import User, Woman, Mentor, Booking
from django.forms import CharField, Select
from datetime import datetime, time


class CustomSignupForm(SignupForm):
    """
    Creating the user model instance based on the selected type
    """
    user_type = forms.ChoiceField(
        choices=User.Type.choices, widget=forms.Select)

    def save(self, request):
        user_type = self.cleaned_data.pop('user_type')
        if user_type == User.Type.WOMAN:
            user = Woman()
        else:
            user = Mentor()

        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']
        user.set_password(self.cleaned_data['password1'])
        user.save()
        return user


class BookingForm(forms.ModelForm):
    message = forms.CharField(
        label='Message', required=True,
        widget=forms.Textarea(
            attrs={'rows': 5, 'placeholder': "Enter your message here ..."}))

    class Meta:
        model = Booking
        fields = ['date', 'time', 'message']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})
        }
