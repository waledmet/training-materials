from django.shortcuts import render, get_object_or_404
from .models import Post


def home(request):
    recent_posts = Post.objects.filter(status='published')[:3]
    context = {
        'recent_posts': recent_posts,
    }
    return render(request, 'home.html', context)


def about(request):
    return render(request, 'about.html')


def post_list(request):
    posts = Post.objects.filter(status='published')
    context = {
        'posts': posts,
    }
    return render(request, 'post_list.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id, status='published')
    return render(request, 'post_detail.html', {'post': post})
