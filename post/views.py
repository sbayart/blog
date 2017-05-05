# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from models import Post

# Create your views here.
def home(request):
    return render(request, "home.html")

def post_list(request):
    posts = Post.objects.all()

    context = {
        "posts" : posts
    }

    return render(request, "post_list.html", context)

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)

    context = {
        "post" : post
    }

    return render(request, "post_detail.html", context)
