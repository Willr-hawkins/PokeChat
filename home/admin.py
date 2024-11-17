from django.contrib import admin
from .models import Post, PostComment

# Register the Post model to the Admin panel
admin.site.register(Post)

# Register the PostComment model to the Admin panel
admin.site.register(PostComment)