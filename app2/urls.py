from django.urls import path
from app2.views import *
app_name = "somthing"

urlpatterns = [
    path("sec/",sec,name="sec"),
]