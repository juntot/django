
from django.contrib import admin
from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^admin/', admin.site.urls, name='admin'),
    url(r'^$', views.index, name='index'),
    url(r'^articles/', include('articles.urls')),
    url(r'^products/', include('products.urls')),
    url(r'^user/', include('users.urls'))
]
