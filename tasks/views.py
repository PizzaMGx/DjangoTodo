from django.shortcuts import render
from django.http import HttpResponse
from .models import Task,SubTask
from django.template import loader

# Create your views here.
def index (response):
    Task_list = Task.objects.order_by('-pub_date')
    template = loader.get_template('index.html')
    context = {
        'task_list': Task_list,
    }
    return HttpResponse(template.render(context, response))