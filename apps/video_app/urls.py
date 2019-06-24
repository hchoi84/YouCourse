from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$', views.index),
    url(r'^(?P<course_id>\d+)/add_video_form$', views.add_video_form),
    url(r'^(?P<course_id>\d+)/add_video_post$', views.add_video_post),
]