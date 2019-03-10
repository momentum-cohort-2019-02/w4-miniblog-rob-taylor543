from django.contrib import admin
from blog.models import BlogPost, Blogger

# Register your models here.

admin.site.register(Blogger)
admin.site.register(BlogPost)
