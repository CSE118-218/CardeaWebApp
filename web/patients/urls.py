from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.getAllActivity, name='index'),
    url(r'^goal$', views.goalActivity, name='goal'),
    url(r'^progress$', views.progressActivity, name='progress'),
    url(r'^progress/update$', views.updateProgress, name='updateProgress'),
]