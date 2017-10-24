from django.conf.urls import url
from django.contrib import admin
from .views import signupp,home


urlpatterns = [
url(r'^$',signupp,name='signup'),
url(r'^home/$',home,name='home'),
]