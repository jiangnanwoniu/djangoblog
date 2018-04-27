__author__ = 'liuhui'

from django.conf.urls import url, include
from blog.views import IndexView, ArticleDetailView, CategoryView, TagView, ArticleEdit, IndexViewMine, ArticleUpdate,ArticleDelete

urlpatterns = [
    url(r'^$', IndexView.as_view(), name="index-view"),
    url(r'^article/(?P<article_id>\d+)/$', ArticleDetailView.as_view(), name='article-view'),
    url(r'^category/(?P<category_id>\d+)/$', CategoryView.as_view(), name='category-view'),
    url(r'^tag/(?P<tag>\d+)/$', TagView.as_view(), name='tag-view'),
    url(r'article_edit/$', ArticleEdit, name='article-edit'),
    url(r'^article_update/(?P<article_id>\d+)/$', ArticleUpdate, name='article-update'),
    url(r'^article_delete/(?P<article_id>\d+)/$', ArticleDelete, name='article-delete'),
    url(r'^article_mine/(?P<author_id>\d+)/$', IndexViewMine.as_view(), name='article-mine'),
]