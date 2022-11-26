from django.urls import path
from translang import views

urlpatterns = [
    path("", views.movetotext),
]
