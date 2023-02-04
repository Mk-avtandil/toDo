from django.shortcuts import render
from django.views.generic import ListView

from .models import ToDo


class Home(ListView):
    model = ToDo
    template_name = 'toDo/index.html'
    context_object_name = 'posts'
