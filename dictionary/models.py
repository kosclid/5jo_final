from django.db import models

# Create your models here.
class Diction(models.Model):
    lang_name = models.CharField(max_length=200)
    lang_text = models.TextField(null=True, blank=True)
    lang_img = models.ImageField(upload_to="media/images/poster")
    lang_initial = models.CharField(max_length=200)