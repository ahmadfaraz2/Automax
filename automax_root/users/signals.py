from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import Profile, Location


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=Profile)
def create_profile_location(sender, instance, created, **kwargs):
    if created:
        profile_location = Location.objects.create()
        instance.location = profile_location
        instance.save()


@receiver(post_delete, sender=Profile)
def delete_profile_location(sender, instance, *args, **kwargs):
    if instance.location:
        instance.location.delete()


# 1) Once a User get created it creates a Profile. For(Line 7 to 10)
# 2) Once a Profile get created it creates a Location. For(Line 14 to 19)


# -----------------------some concept about "instance"---------------------
# "instance.location" is a refference to the "location" field of the
# "Profile" model and "Profile.location" is the actual defination of
# that field in the model.


# When the sender(User) get created it will create the instance of Model(Profile)
# it is attached.


# --------------------------receiver--------------------------------------------|
# It(receiver) expects a signal(post_save) on which it is going to act, which   |
# in this case is going to be the post_save signal.                             |
# The model(User) which is going to act as the sender to who is going to be     |
# the sender of the signal.
