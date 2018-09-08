from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save 

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=None)
    description = models.TextField(max_length=600, default='', blank=True)
    experience = models.TextField(max_length=600, default='', blank=True)
    image = models.ImageField(upload_to="profile_image", default="profile_image/userpicture2.png", blank=True)

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance']) 

post_save.connect(create_profile, sender=User)
