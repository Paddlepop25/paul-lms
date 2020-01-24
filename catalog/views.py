from django.shortcuts import render, redirect, reverse
from .models import Course
from .forms import CourseForm

# Create your views here.
def show_courses(request):
    all_courses = Course.objects.all()
    return render(request, 'catalog/courses.template.html', {
        'all_courses': all_courses
    })
    
def create_course(request):
    if request.method == 'POST':
        create_course_form = CourseForm(request.POST)
        if create_course_form.is_valid():
            create_course_form.save()
            return redirect(reverse(show_courses))

    else:
        create_course_form = CourseForm()

    return render(request, 'catalog/create_course.template.html', {
        'form':create_course_form
    })
        