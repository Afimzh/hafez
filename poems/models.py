from django.db import models

# Create your models here.
class Poems(models.Model):
    title = models.CharField( max_length=50)
    poem_text = models.TextField(max_length=1000) 
    def __str__(self):
        return self.title
    