# This is a URLconf file for mapping URL

from django.conf.urls import url

from .views import index

app_name = 'reservation'
urlpatterns = [
    url(r'^$',index,name='index'),
    url(r'^(?P<id>[0-9]+)/results/$',results,name='results') #TODO: Show the reservation 
]
