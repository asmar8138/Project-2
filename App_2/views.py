from django.shortcuts import render
from django.http import HttpResponse

def function(request):
    return render(request,'customer registration.html')


# Create your views here.
