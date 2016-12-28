from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def add(request):
    num1 = int(request.GET['a'])
    num2 = int(request.GET['b'])
    result = num1 + num2
    return HttpResponse(result)

