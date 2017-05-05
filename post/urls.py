from django.conf.urls import url
from .views import home, post_list, post_detail
from models import Post

urlpatterns = [
    url(r'^$', home),
    url(r'^post/list$', post_list),
    url(r'^post/(?P<post_id>\d+)', post_detail)
]
