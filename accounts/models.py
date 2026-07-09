from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    """
    Extra information about a user that Django's built-in User model
    doesn't have out of the box (phone, address, avatar).

    We link it to User with a OneToOneField: each User has exactly
    one Profile.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100, blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)

    def __str__(self):
        return f'{self.user.username} Profile'


# --------------------------------------------------------------------------
# Signals: automatically create (and save) a Profile every time a new
# User is created, so we never have to remember to do it manually.
# --------------------------------------------------------------------------
@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    else:
        # Profile might not exist yet for users created before this
        # signal existed, so we use get_or_create to be safe.
        Profile.objects.get_or_create(user=instance)
        instance.profile.save()
