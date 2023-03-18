from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager
from datetime import datetime
from cloudinary.models import CloudinaryField


class User(AbstractUser):
    class Type(models.TextChoices):
        WOMAN = "WOMAN", "woman"
        MENTOR = "MENTOR", "mentor"
    type = models.CharField(
        max_length=10, choices=Type.choices)

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
            MentorsProfile.objects.create(user=self)

    def __str__(self):
        return self.username


class MentorsProfile(models.Model):
    mentor_id = models.AutoField(primary_key=True)
    mentor_name = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
        related_name='mentor_profile')
    mentor_image = CloudinaryField('image', default='placeholder')
    mentor_expertise = models.CharField(
        max_length=100, blank=False, null=False)
    mentor_about = models.TextField(blank=False, null=False)
    mentor_years_of_experience = models.PositiveIntegerField(
        blank=True, null=True)
    
    class Meta:
        ordering = ['-mentor_id']

    def __str__(self):
        return f"{self.mentor_name.username} Mentor"


class Booking(models.Model):
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE,
                               related_name="book_mentor")
    user = models.ForeignKey(Woman, on_delete=models.CASCADE,
                             related_name="user")
    date = models.DateField(default=datetime.now)
    time = models.TimeField(default=datetime.now)
    message = models.TextField()

    class Meta:
        unique_together = [['mentor', 'date', 'time']]

    def __str__(self):
        return f"A meeting with {self.mentor} has been booked by {self.user}."
