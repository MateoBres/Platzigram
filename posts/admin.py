from posts.models import Posts
from django.contrib import admin

from posts.models import Posts

# Register your models here.

class PostsAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'photo')

admin.site.register(Posts, PostsAdmin)