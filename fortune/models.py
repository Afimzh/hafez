from django.db import models
from users.models import Customer
class Fortune(models.Model):
    title = models.TextField()
    
    def __str__(self):
        return self.title

