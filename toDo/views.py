from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import ToDo


class Home(ListView):
    model = ToDo
    template_name = 'toDo/index.html'
    context_object_name = 'posts'


class PostDetail(DetailView):
    model = ToDo
    template_name = 'toDo/detail.html'
    context_object_name = 'post'
    slug_url_kwarg = 'post_slug'
