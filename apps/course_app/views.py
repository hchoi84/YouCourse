from django.shortcuts import render, redirect, HttpResponse
from apps.course_app.models import Course, Subject, Category
from django.contrib import messages

def index(request):
    return render(request, "course_app/courses.html")

def create_course_form(request):
    context = {
        'categories': Category.objects.all(),
        'subjects': Subject.objects.all(),
    }
    return render(request, "course_app/create.html", context)

def create_course_post(request):
    if 'user_id' in request.session and request.method == 'POST': #user is logged in and method is post
        errors = Course.objects.validate(request.POST)
        if not errors:
            if request.POST['subject_id']: #subject chosen
                if request.POST['category_id']: #subject chosen category chosen
                    subject_id = request.POST['subject_id']
                    category_id = request.POST['category_id']
                else: #subject chosen category added
                    subject_id = request.POST['subject_id']
                    category_id = Category.objects.create(name = request.POST['category_name']).id
            else: #subject added
                if request.POST['category_id']: #subject added category chosen
                    subject_id = Subject.objects.create(name = request.POST['subject_name']).id
                    category_id = request.POST['category_id']
                else: #subject added category added
                    subject_id = Subject.objects.create(name = request.POST['subject_name']).id
                    category_id = Category.objects.create(name = request.POST['category_name']).id
            course_id = Course.objects.create_course(request.session['user_id'], category_id, subject_id, request.POST).id
        else:
            for key, value in errors.items():
                messages.error(request, value, extra_tags=key)
            return redirect('/course/create_course_form')
        return redirect(f'/course/{course_id}')
    messages.error(request, 'You are not logged in', extra_tags='user_id')
    return redirect('/')

def read_course(request, course_id):
    context = {
        'course': Course.objects.get(id=course_id),
    }
    return render(request, "course_app/read.html", context)

def delete_course(request, course_id):

    return redirect('course')

# NICE TO HAVE...

def edit_course_form(request):
    
    return redirect('course')

def edit_course_post(request):

    return redirect('course')