from django.shortcuts import render
#from django.view.generic import TempleteView
from django.http import HttpResponse

# Create your views here.

#class HomePageView(TempleteView):
 #   def get(self,request,**kwargs):
  #      return render(request, 'index.html', context=None)

def index(request):
    return HttpResponse("Hello World!")

def log_in(request):
    logdict={'insert_key':'This is a template tag'}
    return render(request,'login/index.html',context=logdict)




