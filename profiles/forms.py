from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    """ 
    A form to create a user's profile account.
    """

    class Meta:
        model = UserProfile
        fields = ['profile_image', 'profile_bio']