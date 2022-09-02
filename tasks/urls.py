from django.urls import path
from . import views
from . import apiview

urlpatterns=[
     path('', views.index,name="index"),
     path('<int:task_id>/', views.task_detail, name='task_detail'),
     path('form',views.task_form,name="task_form"),
     path('api', apiview.api,name ="Api_View"),
     path ('api/<int:pk>',apiview.api_task_detail,name= "Api Task Details")
]