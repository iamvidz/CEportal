"""CEportal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from django.conf.urls import url
#from django.urls import include
from django.conf.urls import include
from login import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #path('login/',include('login.urls')),
    #path('index/',views.HomePageView.as_view()),
    #url(r'^log_in/',include('login.urls')),
    #url(r'^$',views.index,name='index'),
    #url(r'^studentlogin/',include('studentlogin.urls')),
    path('studentlogin/',include('studentlogin.urls')),
    path('facultylogin/',include('facultylogin.urls')),
    path('courselist/',include('courselist.urls')),
]
