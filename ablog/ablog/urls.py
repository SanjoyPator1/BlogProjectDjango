
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from theblog import views
from django.conf import settings
from django.conf.urls.static import static

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('theblog.urls')),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),
    path('ckeditor', include('ckeditor_uploader.urls')),
     path('summernote/', include('django_summernote.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)