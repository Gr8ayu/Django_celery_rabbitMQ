from celery.schedules import crontab

CELERY_BEAT_SCHEDULE = {
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