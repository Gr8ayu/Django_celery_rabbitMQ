# Generated by Django 3.1 on 2020-08-07 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=50)),
                ('task_type', models.IntegerField(choices=[(1, 'Task_A'), (2, 'Task_B'), (3, 'Task_C'), (4, 'Task_D'), (5, 'Task_E')])),
            ],
        ),
        migrations.CreateModel(
            name='TaskTracker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_type', models.IntegerField(choices=[(1, 'Task_A'), (2, 'Task_B'), (3, 'Task_C'), (4, 'Task_D'), (5, 'Task_E')])),
                ('update_type', models.CharField(choices=[('daily', 'daily'), ('weekly', 'weekly'), ('monthly', 'monthly')], max_length=10)),
            ],
        ),
    ]
