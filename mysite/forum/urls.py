from django.conf.urls import url
from django.views.generic import ListView, DetailView
from forum.models import Post
from . import views
from .views import createPost

urlpatterns = [
    url(r'^$', ListView.as_view(queryset=Post.objects.all().order_by("-date")[:25], template_name="forum/forum.html")),
    url(r'^(?P<pk>\d+)$', DetailView.as_view(model=Post, template_name='forum/post.html')),
    url(r'^createPost/', createPost.as_view(), name='createPost'),
    url(r'^(?P<pk>[-\w]+)/comment/$', views.add_comment, name='add_comment')
]
 
