from django.conf.urls import patterns, include, url
from posts import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', views.about, name='about'),
	url(r'^blog/', include('posts.urls', namespace="posts")),
    url(r'^admin/', include(admin.site.urls)),
)
