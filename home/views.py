from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Post
from django.utils import timezone


def index(request):
    template = loader.get_template('home/index.html')
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    context= {'posts': posts}
    return HttpResponse(template.render(context, request))
    # POSTS


def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    template = loader.get_template('home/detail.html')
    context = {'post': post}
    return HttpResponse(template.render(context, request))
