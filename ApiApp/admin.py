from django.contrib import admin
from ApiApp.models import Post

# Registering the Post model with the admin site:
admin.site.register(Post)