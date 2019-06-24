from django.shortcuts import render, redirect, HttpResponse

def index(request):

    return render(request, "video_app/index.html")