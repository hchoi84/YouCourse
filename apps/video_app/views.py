from django.shortcuts import render, redirect, HttpResponse

def index(request):

    return render(request, "video_app/index.html")

def add_video_form(request):

    return render(request, "video_app/add.html")

def add_video_post(request, course_id):
    if request.method == 'POST':
        Video.objects.create_video(course_id, request.POST)
    return redirect('video')

def delete_video(request, video_id):
    if request.session['user_id'] == Video.objects.get(id=video_id).User.id:
        Video.objects.delete_video(video_id)
    return redirect('video')

# NICE TO HAVE...

def edit_video_form(request):
    
    return redirect('video')

def edit_video_post(request):

    return redirect('video')