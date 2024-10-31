from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    """ 
    A personal profile to hold personal information
    and both draft and published posts.
    
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(null=True, blank=True)
    profile_bio = models.TextField()

    def __str__(self):
        return f'Profile created for {self.user}.'
