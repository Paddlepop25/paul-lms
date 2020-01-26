from django.urls import path
from .views import index

#  path: name shown on url, function from views, name passed to template
urlpatterns = [
    path('', index)
   ]