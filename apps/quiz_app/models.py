from django.db import models
from apps.course_app.models import *
from apps.user_app.models import *
from apps.video_app.models import *


# Create your models here.
class QuestionManager(models.Manager):
    pass


class Question(models.Model):
    question = models.CharField(max_length=255)
    option1 = models.CharField(max_length=255)
    option2 = models.CharField(max_length=255)
    option3 = models.CharField(max_length=255)
    option4 = models.CharField(max_length=255)
    option5 = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    video = models.ForeignKey(Video, related_name="videos")
    objects = QuestionManager()
