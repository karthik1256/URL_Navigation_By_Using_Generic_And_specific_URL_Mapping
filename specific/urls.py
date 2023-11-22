from specific.views import *
from django.urls import path

app_name='specific'

urlpatterns=[
    path('karthik2/',karthik2,name='karthik2'),
    path('pandu2/',pandu2,name='pandu2'),
]