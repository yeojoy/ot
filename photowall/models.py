from django.db import models

# Create your models here.
class Post(models.Model):
    photo = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)

