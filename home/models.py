from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager
from datetime import datetime, time, timedelta
from django.utils import timezone
from cloudinary.models import CloudinaryField
from django.core.exceptions import ValidationError
import string
import random
from django.utils.text import slugify

TIMES = ((time(16, 00), "16:00"), (time(16, 30), "16:30"), (time(17, 00), "17:00"),
         (time(17, 30), "17:30"), (time(18, 00), "18:00"), (time(18, 30), "18:30"),
         (time(19, 00), "19:30"), (time(19, 30), "20:00"), (time(20, 00), "20:00"),
         (time(20, 30), "20:30"))


def validate_date(date):
    if date <= datetime.now().date():
        raise ValidationError("Date cannot be in the past or the same day.")
    return date


class User(AbstractUser):
    class Type(models.TextChoices):
        WOMAN = "WOMAN", "woman"
        MENTOR = "MENTOR", "mentor"
    type = models.CharField(
        max_length=10, choices=Type.choices)
    slug = models.SlugField(max_length=50, unique=True, default='')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.username)     
        super(User, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.username}"


class WomanManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(
            *args, **kwargs).filter(type=User.Type.WOMAN)


class Woman(User):
    objects = WomanManager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = User.Type.WOMAN
            return super().save(*args, **kwargs)

    def __str__(self):
        return self.username


class MentorManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(
            *args, **kwargs).filter(type=User.Type.MENTOR)


class Mentor(User):
    objects = MentorManager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = User.Type.MENTOR
        super().save(*args, **kwargs)

        # Check if the user has a mentor profile, if not create one
        if not hasattr(self, 'mentor_profile'):
            MentorsProfile.objects.create(mentor_name=self)

    def __str__(self):
        return self.username


class MentorsProfile(models.Model):
    mentor_name = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='mentor_profile')
    slug = models.SlugField(max_length=50,)
    mentor_image = CloudinaryField('image', default='placeholder')
    mentor_expertise = models.CharField(
        max_length=100, blank=False, null=False)
    mentor_about = models.TextField(blank=False, null=False)
    mentor_years_of_experience = models.PositiveIntegerField(
        blank=True, null=True)
    theme = models.CharField(max_length=200, blank=True, null=True)
    location = models.CharField(max_length=254, default='Online')
    date = models.DateField(
        default=(
            datetime.today() + timedelta(
                days=(1 - datetime.today().weekday()) % 7 + 1)).date())
    time = models.TimeField(default='17:00:00')
    link = models.URLField(blank=True, null=True)

    class Meta:
        ordering = ['-id']

    def save(self, *args, **kwargs):
        self.slug = slugify(self.mentor_name)
        super(MentorsProfile, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.mentor_name.username} Mentor"


class Booking(models.Model):
    mentor = models.ForeignKey(
        Mentor, on_delete=models.CASCADE, related_name="book_mentor")
    slug = models.SlugField(max_length=50, default='')
    user = models.ForeignKey(Woman, on_delete=models.CASCADE,
                             related_name="user")
    date = models.DateField(default=datetime.now, validators=[validate_date])
    time = models.TimeField(choices=TIMES, default=time(17, 00))
    message = models.TextField()

    class Meta:
        unique_together = [['mentor', 'date', 'time']]

    def save(self, *args, **kwargs):
        self.slug = slugify(self.mentor)
        super(Booking, self).save(*args, **kwargs)

    def __str__(self):
        return f"A meeting with {self.mentor} has been booked by {self.user}."
