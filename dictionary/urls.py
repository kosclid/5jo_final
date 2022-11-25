from django.urls import path
from dictionary import views

urlpatterns = [
    path("article/", views.article),
    path("home/", views.home),
    path("book/", views.book),
    path("society/", views.society),
    path("qna/", views.qna),

]
