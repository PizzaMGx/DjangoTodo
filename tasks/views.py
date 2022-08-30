from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Task,SubTask
from django.template import loader
from django.urls import reverse

# Create your views here.
def index (response):
    Task_list = Task.objects.order_by('-pub_date')
    template = loader.get_template('index.html')
    context = {
        'task_list': Task_list,
    }
    return HttpResponse(template.render(context, response))

def task_detail(request,task_id):
    task_ret = get_object_or_404(Task, pk=task_id)
    template = loader.get_template('subtask.html')
    subtask_list = task_ret.subtask_set.all()
    context = {
        'subtask_list': subtask_list,
        'task':task_ret
    }
    return (HttpResponse(template.render(context, request)))

def task_form(request):
    template = loader.get_template('form.html')
    return (HttpResponse(template.render()))
    
    