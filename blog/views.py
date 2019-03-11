from django.shortcuts import render
from blog.models import Blogger, BlogPost
from django.views import generic

# Create your views here.

def index(request):
    num_bloggers = Blogger.objects.count()
    num_blogposts = BlogPost.objects.count()

    context = {
        'num_bloggers':num_bloggers,
        'num_blogposts':num_blogposts,
    }

    return render(request, 'index.html', context=context)

class BloggerListView(generic.ListView):
    model = Blogger

class BloggerDetailView(generic.DetailView):
    model = Blogger

class BlogPostListView(generic.ListView):
    model = BlogPost
    paginate_by = 1

class BlogPostDetailView(generic.DetailView):
    model = BlogPost
