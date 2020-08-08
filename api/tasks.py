from celery import shared_task
from celery import Celery
from django.core.mail import send_mail
from celery import app            
from .models import Task, TaskTracker
from celery.schedules import crontab
from datetime import date, timedelta
app = Celery()


        
@app.task
def test():
    print("Success")


@app.task
def sendDailyMail():
    trackers = TaskTracker.objects.filter(update_type = 'daily' )

    message = ""
    for tracker in trackers:
        tracked_task_type = tracker.task_type
        tasks = Task.objects.filter(task_type=tracked_task_type)

        for task in tasks : 
            if task.date_created - date.today() < timedelta(days=1) :
                message = message + task.task_name + ", "


        send_mail(
            'Daily Update for type {} task '.format(tracked_task_type),
            message,
            'emailservice@convin.ai',
            ['support@convin.ai'],
            fail_silently=False,
        )


@app.task
def sendWeeklyMail():
    trackers = TaskTracker.objects.filter(update_type = 'weekly' )

    message = ""
    for tracker in trackers:
        tracked_task_type = tracker.task_type
        tasks = Task.objects.filter(task_type=tracked_task_type)

        for task in tasks : 
            if task.date_created - date.today() < timedelta(days=7) :
                message = message + task.task_name + ", "


        send_mail(
            'Daily Update for type {} task '.format(tracked_task_type),
            message,
            'emailservice@convin.ai',
            ['support@convin.ai'],
            fail_silently=False,
        )


@app.task
def sendMonthlyMail():
    trackers = TaskTracker.objects.filter(update_type = 'monthly' )

    message = ""
    for tracker in trackers:
        tracked_task_type = tracker.task_type
        tasks = Task.objects.filter(task_type=tracked_task_type)

        for task in tasks : 
            
            if task.date_created - date.today() < timedelta(days=30) :
                message = message + task.task_name + ", "


        send_mail(
            'Daily Update for type {} task '.format(tracked_task_type),
            message,
            'emailservice@convin.ai',
            ['support@convin.ai'],
            fail_silently=False,
        )
