from rest_framework import serializers # Import the serializers object model
from .models import Task,SubTask

class TaskSerializer (serializers.Serializer): # Define our serializers same as Models
    # Serializers are used to convert complex data to a more readable format 
    # Create the fields to store the data
    id = serializers.IntegerField(read_only = True)
    task_name = serializers.CharField(required = True, allow_blank=False, max_length=255)
    Task_description = serializers.CharField(required = True, allow_blank = True, max_length = 255)
    Completed = serializers.BooleanField(required=False)
    pub_date = serializers.DateTimeField(required=False)

    #Create method 
    def create(self, validated_data):
        return Task.objects.create(**validated_data) # Takes serialized data and creates a task object 
    # Update method 
    def update(self, instance, validated_data): # Takes serialized data, an object instance and updates that object with the new information
        instance.task_name = validated_data.get("task_name", instance.task_name)
        instance.Task_description = validated_data.get("Task_description", instance.Task_description)
        instance.Completed = validated_data.get("Completed", instance.Completed)
        
        instance.save()
        return instance