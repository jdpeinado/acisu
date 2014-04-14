from django.conf.urls import patterns, url

from posts import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<slug>[^/]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^tag/(?P<tag>[^/]+)/$', views.TagView.as_view(), name='tag'),
)