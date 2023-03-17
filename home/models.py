from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager


class User(AbstractUser):
    class Type(models.TextChoices):
        WOMAN = "WOMAN", "woman"
        MENTOR = "MENTOR", "mentor"

    type = models.CharField(
        max_length=10, choices=Type.choices, default=Type.WOMAN)

    def __str__(self):
        return self.type


class WomanManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(
            *args, **kwargs).filter(type=User.Type.WOMAN)


class Woman(User):
    base_type = User.Type.WOMAN

    objects = WomanManager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = User.Type.WOMAN
            return super().save(*args, **kwargs)


class MentorManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(
            *args, **kwargs).filter(type=User.Type.MENTOR)


class Mentor(User):
    base_type = User.Type.MENTOR

    objects = MentorManager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.type = User.Type.MENTOR
            return super().save(*args, **kwargs)
