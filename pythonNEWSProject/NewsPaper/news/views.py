from django.views.generic import ListView, DetailView
from .models import Post
from pprint import pprint


class PostsList(ListView):
    model = Post
    ordering = '-vremia_sosdania_soobsh'
    template_name = 'posts.html'
    context_object_name = 'posts'


class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'




