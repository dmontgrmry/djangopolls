from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'), # /polls/
    url(r'^(?P<question_id>[0-9]+)$', views.detail, name='detail'), # /polls/6/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'), # /polls/6/results/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'), # /polls/6/vote/
]
