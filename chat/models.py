from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


# User Profile Model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField('self', related_name='followed_by', symmetrical=False, blank=True)
    profile_pic = models.ImageField(default='static/chat/images/default-profile-photo.jpg', null=True, blank=True, upload_to='images/profile/')

    def __str__(self):
        return self.user.username


# Create Profile When New User Signs Up
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()


post_save.connect(create_profile, sender=User)

