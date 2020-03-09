from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def studentlogin(request):
    return render(request,'studentlogin/slide.html')