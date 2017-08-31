from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import login, logout
from ckeditor.fields import RichTextField


urlpatterns = [
    url(r'^login$', login, name='login'),
    url(r'^logout$', logout, name='logout'),
    url(r'^admin/', admin.site.urls),
    url(r'^', include('post.urls')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
