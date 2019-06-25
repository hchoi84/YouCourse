from django.shortcuts import render, redirect, HttpResponse
from . import models

def index(request):
    return render(request, "course_app/courses.html")

def create_course_form(request):

    return render(request, "course_app/create.html")

def create_course_post(request):
    if 'user_id' in request.session and request.method == 'POST':
        Course.objects.create_course(request.session['user_id'], request.form)
    return redirect('/course')

def read_course(request, video_id):

    return redirect('course')

def delete_course(request, video_id):

    return redirect('course')

# NICE TO HAVE...

def edit_course_form(request):
    
    return redirect('course')

def edit_course_post(request):

    return redirect('course')