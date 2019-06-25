from django.db import models
from apps.user_app.models import *


class CourseManager(models.Manager):

    def create_course(self, user_id, form):
        new_course = self.create(subject = form['subject'], category = form['category'], title = form['title'], description = form['description'], author = User.objects.get(id = user_id))
        return self
    
    def delete_course(self, course_id):
        self.get(id = course_id).delete()
        return self

    def edit_course(self, course_id, form):
        course = self.get(id = course_id)
        course.subject = form['subject']
        course.category = form['category']
        course.title = form['title']
        course.description = form['description']
        course.save()
        return self


class Category(models.Model):
    name = models.CharField(max_length=255)


class Subject(models.Model):
    name = models.CharField(max_length=255)


class Course(models.Model):
    title = models.CharField(max_length=255)
    subject = models.ForeignKey(Subject,related_name="courses")
    category = models.ForeignKey(Category,related_name="courses")
    description = models.TextField()
    likes = models.IntegerField(default=0)
    author = models.ForeignKey(User, related_name="courses_authored")
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    objects = CourseManager()

