from django.urls import path
from .views import show_courses, create_course

urlpatterns = [
    path('', show_courses),
    path('create', create_course)
   ]