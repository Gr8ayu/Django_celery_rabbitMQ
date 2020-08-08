from django.db import models
from datetime import date
# Create your models here.

TASK_TYPES = [
    (1, 'Task_A'),
    (2, 'Task_B'),
    (3, 'Task_C'),
    (4, 'Task_D'),
    (5, 'Task_E'),
]
UPDATE_TYPES = [
    ('daily', 'daily'),
    ('weekly', 'weekly'),
    ('monthly', 'monthly'),
]


class Task (models.Model):
    task_name = models.CharField(max_length=50)
    task_type = models.IntegerField(choices=TASK_TYPES)
    date_created = models.DateField(auto_now_add=True)
    def __str__ (self):
        return self.task_name + " : " + str(self.task_type)


class TaskTracker(models.Model):
    task_type = models.IntegerField(choices=TASK_TYPES)
    update_type = models.CharField(max_length=10, choices=UPDATE_TYPES)

    def __str__ (self):
        return str(self.task_type) +" : "+ self.update_type

