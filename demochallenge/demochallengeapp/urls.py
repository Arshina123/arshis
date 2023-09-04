from . import views
from django.urls import path

urlpatterns = [

    path('',views.demo,name='demo'),
    path('add/',views.model,name='addition'),
    path('sub/',views.model,name='subtraction'),
    path('mul/',views.model,name='multiplication'),
    path('div/',views.model,name='division')
]