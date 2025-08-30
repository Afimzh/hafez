from django.db import models
from users.models import Customer
class Fortune(models.Model):
    fortune_poem = models.TextField()
    fortune_user = models.ForeignKey(Customer, on_delete=models.CASCADE)

