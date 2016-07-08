"""puppet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url,patterns
from django.contrib import admin
import settings

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','osweb.views.index'),
    url(r'^nodes/(.*)/$','osweb.views.nodes',name='nodes'),
    url(r'^remote/$','osweb.views.remote'),
    url(r'^vnc_auto/$','osweb.views.vnc_auto'),
    url(r'^config/$','osweb.views.config'),
    url(r'^report/$','osweb.views.report'),
    url(r'^export/$','osweb.views.export'),
    url(r'^run/$','osweb.views.run'),
    url(r'^login/$','osweb.views.login'),
    url(r'^logout/$','osweb.views.logout'),
    url(r'^dashboard/$','osweb.views.dashboard'),
    url(r'^status/$','osweb.views.status'),
]
