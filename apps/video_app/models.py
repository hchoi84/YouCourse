from django.db import models
from apps.user_app.models import User
from apps.course_app.models import Course

class VideoManager(models.Manager):
    
    def add_video(self, course_id, form):
        new_video = self.create(url = form['url'], description = form['description'], likes = 0, course = Course.objects.get(id = course_id))
        return self
    
    def remove_video(self, video_id):
        video = self.get(id = video_id).delete()
        return self

    def edit_video(self, video_id, form):
        video = self.get(id = video_id)
        video.url = form['url']
        video.description = form['description']
        


class Video(models.Model):
    url = models.CharField(max_length=255)
    description = models.TextField()
    likes = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    course = models.ForeignKey(Course, related_name='videos')
    users_who_completed = models.ManyToManyField(User, related_name="videos_completed")
    objects = VideoManager()

