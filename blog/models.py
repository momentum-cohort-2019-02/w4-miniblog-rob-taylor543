from django.db import models
from django.urls import reverse

# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length = 255)
    blogger = models.ForeignKey('Blogger', on_delete=models.SET_NULL, null = True)
    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the blog post')
    post_date = models.DateField(auto_now_add=True)
    content = models.TextField(max_length=10000, help_text='Write your post here')

    class Meta:
        ordering = ['post_date']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blogpost-detail", kwargs={"pk": self.pk})


class Blogger(models.Model):
    screen_name = models.CharField(max_length = 20)
    bio = models.TextField(max_length=1000, help_text='Enter a brief bio')

    class Meta:
        ordering = ['screen_name']

    def __str__(self):
        return self.screen_name

    def get_absolute_url(self):
        return reverse("blogger-detail", kwargs={"pk": self.pk})
    
