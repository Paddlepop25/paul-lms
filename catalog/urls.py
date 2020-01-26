from django.urls import path
from .views import show_courses, create_course, update_course

urlpatterns = [
    path('', show_courses, name='show_courses'),
    path('create', create_course),
    path('update/<course_id>', update_course, name='update_course')
   ]