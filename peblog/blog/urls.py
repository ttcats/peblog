#encoding:utf-8
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    #url(r'page/(\d+)$', views.page, name='page'),
    url(r'articles/(\d{4})$', views.blog, name='article'),
    url(r'tags/(.*)/$', views.tag, name='tag'),
    url(r'archives/(\d{4}-\d{2})/$', views.archive, name='archive'),
    ]
