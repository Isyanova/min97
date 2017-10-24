from django.contrib import admin
from .models import Post
from .models import Comment, Subject

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Subject)
