from django.urls import path,include, re_path
from . import views

urlpatterns = [
    
    path('addtask/', views.addTask.as_view()),
    path('addtracker/', views.addTracker.as_view()),
    
    path('gettask/', views.getTask.as_view()),
    path('gettracker/', views.getTracker.as_view()),


]