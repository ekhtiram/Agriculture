from django.conf.urls import url,include
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url('^', include('django.contrib.auth.urls')),
    url(r'^home/', views.home, name='home'),
    url(r'^gallery/', views.gallery, name='gallery'),
    url(r'^contact/', views.contact, name='contact'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
