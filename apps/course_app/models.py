from django.db import models
from apps.user_app.models import *


class CourseManager(models.Manager):
    pass


# Create your models here.
class Course(models.Model):
    subject = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    description = models.TextField()
    author = models.ForeignKey(User, related_name="courses_authored")
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    objects = CourseManager()