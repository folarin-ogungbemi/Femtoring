from django.dispatch import receiver
from django.db.models.signals import post_save
from home.models import User, MentorsProfile


@receiver(post_save, sender=User)
def create_mentors_profile(sender, instance, created, **kwargs):
    """
    Creates a Mentors Profile instance when a Mentor User is created.
    """
    print(f"User Type: {instance.type}")
    if created:
        if instance.type == 'MENTOR':
            MentorsProfile.objects.create(user=instance)
            print("mentor created successfully!")
