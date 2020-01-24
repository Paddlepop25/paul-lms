from django.urls import path
from .views import show_courses

urlpatterns = [
    path('', show_courses)
   ]