from django.db import models

# Create your models here.
class Domestic(models.Model):
    img = models.ImageField(upload_to='pics')
    name= models.CharField(max_length=100)
    desc = models.TextField()
    cost = models.IntegerField()