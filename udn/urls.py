from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'participant/$', views.participant_add),
    url(r'participant/results/$', views.participant_results)
]