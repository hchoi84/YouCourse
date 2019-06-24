from django.db import models
from apps.quiz_app.models import *
from apps.user_app.models import *
from apps.course_app.models import *

class VideoManager(models.Manager):
    pass


class Video(models.Model):
    url = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    course = models.ForeignKey(Course, related_name='videos')
    users_who_completed = models.ManyToManyField(User, related_name="videos_completed")
    objects = UserManager()

