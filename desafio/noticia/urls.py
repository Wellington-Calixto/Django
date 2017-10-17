from django.conf.urls import url

from . import views

app_name='noticia'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.categoria_view, name='categoria'),
    url(r'^(?P<pk>[0-9]+)/noticia/$', views.noticia_view, name='noticia'),
    ]