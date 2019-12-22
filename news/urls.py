from django.conf.urls import url

from . import views

app_name = 'news'

urlpatterns = [
    url(r'^$', views.index, name='news-index'),
    # url(r'^(?P<news_id>[0-9]+)/$', views.detail, name='news-detail'),
    url(r'^(?P<slug>[\w-]+)/$', views.detail, name='news-detail'),
]
