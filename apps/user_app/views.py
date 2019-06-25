from django.shortcuts import render, redirect, HttpResponse
from .models import User
from apps.video_app.models import Video
from apps.course_app.models import Course
from django.contrib import messages

def index(request):
    return render(request, 'user_app/index.html')

def register_user(request):
    # validate user information
    errors = User.objects.register_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
        return redirect("/")

    # register user
    request.session['uid'] = User.objects.register_user(request.POST)
    return redirect("/courses")

def login(request):
    # validate login info
    errors = User.objects.login_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
        return redirect("/")
     
    # login
    request.session['uid'] = User.objects.get(email=request.POST['email']).id
    # request.session['hashed_uid'] = str(User.objects.hash_id(request.session['uid']))
    return redirect("/courses")

def profile(request, uid):
    # if not 'uid' in request.session:
    #     messages.error(request, "Please log in", extra_tags="log_in")
    #     return redirect("/")
    user = User.objects.get(id=uid)
    completed = Video.objects.filter(users_who_completed=user)
    created = Course.objects.filter(author=user)
    context={
        "user": user,
        "completed": completed,
        "created": created,
    }
    return render(request, "user_app/profile.html", context)

def logout(request):
    keys = []
    for key in request.session.keys():
        keys.append(key)
    for key in keys:
        del request.session[key]
    return redirect("/")
