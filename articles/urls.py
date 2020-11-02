
from django.conf.urls import url
from django.urls import path, re_path
from . import views
app_name = 'articles'

urlpatterns = [
    url(r'^$', views.article),
    # url(r'^(?P<slugs>[\w-]+)/$', views.article_detail, name='detail')
    path('<slug:slugs>', views.article_detail, name='detail')
]


