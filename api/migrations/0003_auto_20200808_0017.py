# Generated by Django 3.1 on 2020-08-08 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_task_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date_created',
            field=models.DateField(auto_now_add=True),
        ),
    ]
