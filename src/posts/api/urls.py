from django.conf.urls import url
from django.contrib import admin

from .views import (
    PostDetailAPIView,
    PostUpdateAPIView,
    PostDeleteAPIView,
    PostListAPIView
	)

urlpatterns = [
	url(r'^$', PostListAPIView.as_view(), name='list'),
    # url(r'^create/$', post_create),
    url(r'^(?P<slug>[\w-]+)/$', PostDetailAPIView.as_view(), name='detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', PostUpdateAPIView.as_view(), name='update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', PostDeleteAPIView.as_view(), name='delete'),
    # url(r'^posts/$', "<appname>.views.<function_name>"),
]