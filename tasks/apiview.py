from urllib import response
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Task,SubTask
from django.template import loader
from django.urls import reverse
from .forms import addtaskForm
from .serializers import TaskSerializer
import datetime
# Create your views here.

@csrf_exempt # Bypass the csrf token verification of django
def api(request): # List all objects of the database using serializers More Info: https://khalsalabs.com/csrf-exempt-in-django/
        if request.method == 'GET':  
            task_list = Task.objects.all()
            serializer = TaskSerializer(task_list, many=True) # You can also Create serializers with several objects using the arg many = True
            return JsonResponse(serializer.data, safe=False) # Return the json data
        elif request.method == "POST": 
            data = JSONParser().parse(request) # Parse the request into JSON
            serializer = TaskSerializer(data=data) # Create the serializer from the data
            if serializer.is_valid():
                serializer.save() # Save it in the database 
                return JsonResponse(serializer.data, status = 201)
            return JsonResponse(serializer.errors, status = 401)
            
@csrf_exempt
def api_task_detail(request, pk): # Take the ID in the url
    try:
        task = Task.objects.get(id = pk) # Get the object
    except Task.DoesNotExist:
        return HttpResponse(status = 404)
    
    if request.method == "GET": 
        serializer = TaskSerializer(task)
        return JsonResponse(serializer.data)
    
    elif request.method == "PUT": # Modify the current Data in te object 
        data = JSONParser().parse(request)
        serializer = TaskSerializer(task, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse (serializer.errors, status = 400)

    elif request.method == "DELETE": # Delete the object
        task.delete()
        return HttpResponse(status = 204)


