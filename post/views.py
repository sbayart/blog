# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.decorators import permission_required
from models import Post, Category
from forms import PostForm
from ckeditor.fields import RichTextField

# Create your views here.
def home(request):
    return render(request, "home.html")

def post_list(request):
    cats = Category.objects.all()

    category = request.GET.get("cat", None)
    if category != None:
        posts = Post.objects.filter(category = category)
        paginator = Paginator(posts, 15) # Show 25 contacts per page
    else:
        posts = Post.objects.all()
        paginator = Paginator(posts, 15) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
         # If page is not an integer, deliver first page.
        posts = paginator.page(1)
    except EmptyPage:
         # If page is out of range (e.g. 9999), deliver last page of results.
        posts = paginator.page(paginator.num_pages)

    context = {
        "cats" : cats,
        "posts" : posts,
        "selected_cat" : category
    }

    return render(request, "post_list.html", context)

def post_detail(request, post_slug):
    post = Post.objects.get(slug = post_slug)

    context = {
        "post" : post
    }

    return render(request, "post_detail.html", context)

@login_required
@permission_required('post.add_post')
def post_create(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('post-detail', post_slug = post.slug)

    context = {
        "form" : form
    }

    return render(request, "post_create.html", context)

@login_required
@permission_required('post.change_post')
def post_edit(request, post_slug):
    post = Post.objects.get(slug = post_slug)
    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('post-detail', post_slug = post.slug)

    context = {
        "form" : form,
        "post" : post
    }
    return render(request, "post_edit.html", context)

@login_required
@user_passes_test(lambda u: u.is_superuser)
def post_delete(request, post_slug):
    postdelete = Post.objects.get(slug = post_slug)
    postdelete.delete()

    return redirect('post-list')
