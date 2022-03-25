from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy


# Create your views here.
class PostListView(ListView):
    template_name = "posts/list.html"
    model = Post


class PostDetailView(DetailView):
    template_name = "posts/detail.html"
    model = Post


class PostCreateView(CreateView):
    template_name = "posts/new.html"
    model = Post
    fields = ['title', 'text']


class PostUpdateView(UpdateView):
    template_name = "posts/edit.html"
    model = Post
    fields = ['title', 'text']


class PostDeleteView(DeleteView):
    template_name = "posts/delete.html"
    model = Post
    success_url = reverse_lazy('posts_list')
