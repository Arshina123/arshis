from django.shortcuts import render
# from . models import Place
from . models import Team
# Create your views here.
from django.http import HttpResponse

def demo(request):
    obj = Team.objects.all()
    return render(request,"index.html",{'result':obj})

