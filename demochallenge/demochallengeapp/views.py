from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def demo(request):
    name="hai"
    return render(request,'index.html',{'obj':name})
def model(result):
    x=int(result.GET['num1'])
    y=int(result.GET['num2'])
    res=x+y
    res1=x-y
    res2=x*y
    res3=x/y
    return render(result,'result.html',{'addition':res,'subtraction':res1,'multiplication':res2,'division':res3})

