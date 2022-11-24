from django.urls import path
from translang import views

urlpatterns = [
    path("", views.home1),
    path("home/send/", views.home),
    path("test/", views.test),
]
