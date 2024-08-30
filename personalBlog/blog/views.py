from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin

def home(request):
    return render(request, "navbar.html")

def post_view(request, pk):
    posts = Post.objects.all()

    for post in posts:
        print(post.title)

    return render(request, "home.html", {"posts": posts})