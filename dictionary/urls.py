from django.urls import path
from dictionary import views

urlpatterns = [
    path("article/", views.article),
    path("home/", views.home),
    path("book/", views.book),
    path("society/", views.society),
    path("society/new/", views.new_post),
    path("society/<int:pk>/", views.single_post),
    path("society/<int:pk>/comment/", views.post_comment),
    path("qna/", views.qna),
    path("test/", views.test),

]
