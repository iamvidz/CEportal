
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def courselist(request):
    return render(request,'courselist/index.html')

def viewcourse(request):
    return render(request,'courselist/index.html')