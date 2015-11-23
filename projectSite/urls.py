"""projectSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from report import urls as report_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^report/', include(report_urls))
"""

from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve


import postman

urlpatterns = [

    # url(r'^admin/', include(admin.site.urls)),
    url(r'^reports/', include('reports.urls')),
    url(r'^', include('index.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^messages/', include('postman.urls', namespace='postman', app_name='postman')),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT})

]
