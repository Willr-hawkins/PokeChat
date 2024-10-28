from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, 'Draft'), (1, 'Published'))

class Post(models.Model):
    """ Stores a single post entry realted to :model:`auth.User`. """
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts'
    )
    post_image = models.ImageField(null=True, blank=False)
    post_caption = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f'post by {self.author}.'