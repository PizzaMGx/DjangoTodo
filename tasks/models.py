from django.db import models
from django.utils import timezone
import datetime

class Task(models.Model): #table
    task_name = models.CharField(max_length=200) #Field or column
    Task_despcription = models.CharField(max_length=500) #Field or column
    pub_date = models.DateTimeField('date published')
    
class SubTask(models.Model):
    subtask = models.ForeignKey(Task, on_delete=models.CASCADE)
    subtask_text = models.CharField(max_length=200)