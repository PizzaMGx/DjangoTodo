from urllib import response
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Task,SubTask
from django.template import loader
from django.urls import reverse
from .forms import addtaskForm
import datetime
# Create your views here.
def index (request):
    Task_list = Task.objects.order_by('-pub_date')
    template = loader.get_template('index.html')
    context = {
        'task_list': Task_list,
    }    

    return HttpResponse(template.render(context, request))

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
    print({"requestDebug: ": request})
    if(request.GET.get('addsubtask')):
        print ({"test":1})
    else:
        
        print (request.GET.get("addsubtask"))
    if (request.method == "POST"):
        create_task = addtaskForm(request.POST) # check if the current method is post
        if create_task.is_valid():
            task_n = create_task.cleaned_data["task_name"]
            task_d = create_task.cleaned_data["task_description"]
            task_c = create_task.cleaned_data["Completed"] #Store the data

            save_task = Task(task_name = task_n, Task_despcription = task_d, Completed = task_c, pub_date= datetime.datetime.now()) #Create the Model object
            save_task.save() # save the model object
    create_task = addtaskForm
    return render(request, "form.html", {"form":create_task})
    
    