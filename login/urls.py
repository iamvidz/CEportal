from django.conf.urls import url
from login import views


urlpatterns=[
    #url(r'^$',views.index,name='index'),
    url(r'^$',views.log_in,name='log_in'),
    
]
