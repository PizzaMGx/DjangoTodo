from django import forms

class addtaskForm(forms.Form):
    task_name = forms.CharField(label = "Task Name")
    task_description = forms.CharField(label="Task Description")
    Completed = forms.BooleanField(label="Completed", required=False)