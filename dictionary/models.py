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