from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    """
    A user profile model for creating a custom profile,
    to display a unique persona.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(null=True, blank=True)
    profile_bio = models.TextField(max_length=250)

    def __str__(self):
        return f'Successfully created profile for {self.user}.'
