from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.getAllActivity, name='index'),
    url(r'^goal$', views.goalActivity, name='query'),
]