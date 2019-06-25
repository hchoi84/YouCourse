from django.shortcuts import render, redirect, HttpResponse

def index(request):

    return render(request, "video_app/index.html")

def add_video_form(request):

    return render(request, "video_app/index.html")

def add_video_post(request):

    return redirect('video')

def edit_video_form(request):
    
    return render(request, "video_app/index.html")

def edit_video_post(request):

    return redirect('video')

def delete_video(request):

    return redirect('video')