# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from autoslug import AutoSlugField
from ckeditor.fields import RichTextField

from django.db import models

# Create your models here.

class Category(models.Model):
    label = models.CharField(verbose_name="Catégorie", max_length=50)

    def __unicode__(self):
        return "{0}" . format(self.label)
    #
    # class Meta:
    #     verbose_name = "Categorie"

class Post(models.Model):
    title = models.CharField(verbose_name="Titre", max_length=50)
    body = RichTextField(verbose_name="Contenu", )
    creation_date = models.DateTimeField(auto_now_add=True)
    slug = AutoSlugField(populate_from='title', unique_with='title')
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
    )
    def __unicode__(self):
        return "{0}" . format(self.title)

    class Meta:
            verbose_name = "Article"
