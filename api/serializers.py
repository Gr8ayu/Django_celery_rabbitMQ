from rest_framework import serializers
from .models import Task, TaskTracker


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class TrackerSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskTracker
        fields = '__all__'