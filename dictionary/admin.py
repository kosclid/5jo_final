from django.contrib import admin
from .models import Dictionganada, Post, Post_Comment, Article, SignDonate

# Register your models here.
admin.site.register(Dictionganada)
admin.site.register(Post)
admin.site.register(Post_Comment)
admin.site.register(Article)
admin.site.register(SignDonate)

