
from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^courses/',views.courselist,name='courselist')
]