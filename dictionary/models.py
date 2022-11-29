from django.db import models
from accounts.models import User


# Create your models here.
class Dictionganada(models.Model):
    lang_name = models.CharField(max_length=200)
    lang_text = models.TextField(null=True, blank=True)
    lang_img = models.ImageField(upload_to="media/images/ganadara")
    lang_initial = models.CharField(max_length=200)


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_column="user")
    post_name = models.CharField(max_length=200)
    post_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}  : {self.post_name}"


class Post_Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_column="user")
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}  : {self.post} : {self.user}"


class Article(models.Model):
    art_name = models.CharField(max_length=200)
    art_link = models.CharField(max_length=200)
    art_from = models.CharField(max_length=200)
    art_img = models.ImageField(upload_to="media/images/article")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.art_name}"


class SignDonate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_column="user")
    lang_name = models.CharField(max_length=200)
    lang_text = models.TextField(max_length=200)
    donate_file = models.FileField(upload_to="media/video")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.lang_name} : {self.user}"