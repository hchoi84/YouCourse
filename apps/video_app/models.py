from django.db import models
from apps.user_app.models import User
from apps.course_app.models import Course

class VideoManager(models.Manager):
    
    def create_video(self, course_id, form):
        url = "https://www.youtube.com/embed/" + form['url'].split('=')[-1] #splits the video id out of the full url then concats to the YouTube embed path
        new_video = self.create(title = form['title'], url = url, description = form['description'], likes = 0, course = Course.objects.get(id = course_id))
        return self
    
    def delete_video(self, video_id):
        self.get(id = video_id).delete()
        return self

    def edit_video(self, video_id, form):
        video = self.get(id = video_id)
        video.url = form['url']
        video.description = form['description']
        video.save()
        return self
        
class Video(models.Model):
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    description = models.TextField()
    likes = models.IntegerField(default=0)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    course = models.ForeignKey(Course, related_name='videos')
    users_completed = models.ManyToManyField(User, related_name="videos_completed")
    objects = VideoManager()