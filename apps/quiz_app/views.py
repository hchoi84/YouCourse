from django.shortcuts import render, redirect, HttpResponse
from .models import Question
from apps.video_app.models import Video

def index(request):
    # video = Video.objects.get(id=1)
    # questions = Question.objects.filter(video=video)
    return render(request, "quiz_app/quiz.html")

def test(request):
    print(request.POST)
    return redirect("/quiz")