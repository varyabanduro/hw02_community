from django.shortcuts import render, get_object_or_404
from .models import Post, Group

COUNT = 10


def index(request):
    template = 'posts/index.html'
    posts = Post.objects.all()[:COUNT]
    context = {
        'posts': posts
    }
    return render(request, template, context)


def group_posts(request, slug):
    groups = get_object_or_404(Group, slug=slug)
    template = 'posts/group_list.html'
    title = groups.title
    posts = Post.objects.filter(group=groups).all()[:COUNT]
    context = {
        'title': title,
        'groups': groups,
        'posts': posts
    }
    return render(request, template, context)
