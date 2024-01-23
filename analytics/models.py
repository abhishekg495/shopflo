from django.db import models

# Create your models here.
class Post(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    content = models.TextField()

    def __str__(self):
        return self.content
