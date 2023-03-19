from django.dispatch import receiver
from django.db.models.signals import post_save
from home.models import User, MentorsProfile


@receiver(post_save, sender=User)
def create_mentors_profile(sender, instance, created, **kwargs):
    """
    Creates a Mentors Profile instance when a Mentor User is created.
    """
    if created and instance.type == 'MENTOR':
        MentorsProfile.objects.create(mentor_name=instance)

