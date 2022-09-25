from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^reg_user$', views.reg_user, name='reg_user'),
]
