from django.db import models
from poems.models import Poems
from users.models import Customer
# Create your models here.
class Favorite(models.Model):
    title = models.CharField( max_length=50)
    favorites_poem = models.ForeignKey(Poems , on_delete=models.CASCADE)
    favorites_user = models.ForeignKey(Customer , on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.favorites_user} - {self.favorites_poem.title}"
    