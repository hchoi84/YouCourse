from django.shortcuts import render, redirect, HttpResponse
from apps.video_app.models import Video
from apps.course_app.models import Course, Subject, Category
from django.contrib import messages

def create_video_form(request, course_id):
    context = {
        'course': Course.objects.get(id=course_id),
    }
    return render(request, "video_app/create.html", context)

def create_video_post(request, course_id):
    if 'user_id' in request.session and request.method == 'POST':
        errors = Video.objects.validate(request.POST)
        if not errors:
            video_id = Video.objects.create_video(course_id, request.POST).id
            return redirect(f'/course/{course_id}/video/{video_id}')
        else:
            for key, value in errors.items():
                messages.error(request, value, extra_tags=key)
            return redirect(f'/course/{course_id}/create_video_form')
    messages.error(request, 'You are not the author of this course', extra_tags='user_id')
    return redirect(f'/course/{course_id}')

def read_video(request, course_id, video_id):
    video = Video.objects.get(id=video_id)
    context = {
        'title': video.title,
        'url': video.url,
        'description': video.description,
        'likes': video.likes,
        'course': Course.objects.get(id=course_id),
        'author': int(request.session['user_id']) == int(Course.objects.get(id=course_id).author.id),
    }
    return render(request, "video_app/read.html", context)

def delete_video(request, course_id, video_id):
    if request.session['user_id'] == Video.objects.get(id=video_id).User.id:
        Video.objects.delete_video(video_id)
    return redirect('video')

def edit_video_form(request, course_id, video_id):
    video = Video.objects.get(id=video_id)
    context = {
        'title': video.title,
        'url': video.url,
        'description': video.description,
        'likes': video.likes,
    }
    return render(request, "video_app/add.html", context)

def edit_video_post(request, course_id, video_id):

    return redirect('video')