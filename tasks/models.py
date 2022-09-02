from django.db import models
from django.utils import timezone
import datetime

class Task(models.Model): #table
    task_name = models.CharField(max_length=200) #Field or column
    Task_description = models.CharField(max_length=500) #Field or column
    Completed = models.BooleanField()
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return (self.task_name)
    
class SubTask(models.Model):
    task_asociated = models.ForeignKey(Task, on_delete=models.CASCADE)
    subtask_text = models.CharField(max_length=200)
    def __str__(self):
        return (self.subtask_text)