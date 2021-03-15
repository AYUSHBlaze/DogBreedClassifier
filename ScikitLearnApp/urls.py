from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'imageupload', include('imgUpload.urls')),
    url(r'^admin/', admin.site.urls), 
]