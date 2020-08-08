from __future__ import absolute_import, unicode_literals
from celery.schedules import crontab

import os

from celery import Celery

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'convin.settings')

app = Celery('convin')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    
    'test-update': {
        'task': 'api.tasks.sendDailyMail',
        'schedule': 60,
        
    },
    # Executes every day at 5:00 PM
    'daily-update': {
        'task': 'api.tasks.sendDailyMail',
        'schedule': crontab(hour=17),
        
    },
    # Executes every Monday morning at 7:30 a.m.
    'weekly-update': {
        'task': 'api.tasks.sendWeeklyMail',
        'schedule': crontab(hour=7, minute=30, day_of_week=1),
        
    },
    'monthly-update': {
        'task': 'api.tasks.sendMonthlyMail',
        'schedule': crontab(hour=7, minute=30, day_of_month=1),
        
    },
}


# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))