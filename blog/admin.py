from django.contrib import admin
from .models import Post


# Register the Post model so it appears in the admin panel
admin.site.register(Post)
