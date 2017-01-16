from django.conf.urls import url
from django.contrib import admin
from . import views

app_name = 'service'

urlpatterns = [

    url(r'^$', views.login_user, name='login'),

    url(r'^register/$', views.UserFormView.as_view(), name='register'),

    url(r'^index/$', views.IndexView.as_view(), name='index'),

    url(r'^login_user/$', views.login_user, name='login_user'),

    url(r'^logout_user/$', views.logout_user, name='logout_user'),

    #/services/<ordem_id>/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    url(r'ordem_de_servico/add/$', views.CreateOrdem.as_view(), name='ordem-add'),

    url(r'ordem_de_servico/(?P<pk>[0-9]+)/$', views.UpdateOrdem.as_view(), name='ordem-update'),

    #/service/<pk>/delete
    url(r'ordem_de_servico/(?P<pk>[0-9]+)/delete/$', views.DeleteOrdem.as_view(), name='ordem-delete'),


]
