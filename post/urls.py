from django.conf.urls import url
from .views import home, post_list, post_detail, post_create, post_edit, post_delete
from models import Post, Category
from ckeditor.fields import RichTextField

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^post/list$', post_list, name='post-list'),
    url(r'^post/create$', post_create, name='post-create'),
    url(r'^post/(?P<post_slug>[\w-]+)/edit$', post_edit, name='post-edit'),
    url(r'^post/(?P<post_slug>[\w-]+$)', post_detail, name='post-detail'),
    url(r'^post/(?P<post_slug>[\w-]+)/delete$', post_delete, name='post-delete')
]
