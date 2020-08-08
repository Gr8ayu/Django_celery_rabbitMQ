from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Task, TaskTracker
from .serializers import TaskSerializer, TrackerSerializer


# API to list all Tasks available
# @params : None
# methods : GET 
# endpoint: /api/gettask

class getTask(APIView):

    def get(self,request):
        data = Task.objects.all()
        serializer = TaskSerializer(data, many=True)
        data = serializer.data
        return Response(data) # Return JSON



# API to list all Trackers available
# @params : None
# methods : GET 
# endpoint: /api/gettracker


class getTracker(APIView):
    def get(self,request):
        data = TaskTracker.objects.all()
        serializer = TrackerSerializer(data, many=True)
        data = serializer.data
        return Response(data) # Return JSON


# API to add new Task 
# @params : task_name, task_type
# methods : POST
# endpoint: /api/addtask

class addTask(APIView):

    def post(self,request):
        requestData = request.data 
        serializer = TaskSerializer(data = requestData)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)


# API to add new Task 
# @params : update_type, task_type
# methods : POST
# endpoint: /api/addtracker


class addTracker(APIView):

    def post(self,request):
        requestData = request.data 
        serializer = TrackerSerializer(data = requestData)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)
