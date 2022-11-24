from django.urls import path
from detail import views

urlpatterns = [
    path("", views.home1),
    path("home/send/", views.home),
    path("test/", views.test),
]
