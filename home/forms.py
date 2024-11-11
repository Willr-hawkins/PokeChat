from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    """ 
    A form to create a new post entry related to the Post model. 
    """

    class Meta:
        model = Post
        fields = ['post_image', 'post_caption', 'status']

class UpdateStatusForm(forms.ModelForm):
    """
    A form to update a existing posts status.
    """

    class Meta:
        model = Post
        fields = ['status']