# -*- coding: utf-8 -*-
from django import forms
from models import Post, Category
from ckeditor.fields import RichTextField



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"
