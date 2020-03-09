from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse



def facultylogin(request):
    return render(request,'facultylogin/slide.html')