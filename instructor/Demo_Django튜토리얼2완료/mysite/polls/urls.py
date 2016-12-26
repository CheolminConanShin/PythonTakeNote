# encoding:utf-8
from django.conf.urls import include, url 
from . import views 

urlpatterns = [
    url(r'^polls/', include('polls.urls')),
    url(r'^$', views.index, name='index'),
    ]
