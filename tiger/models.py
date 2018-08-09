from django.db import models
from django.db.models.fields import CharField
from unittest.util import _MAX_LENGTH

# Create your models here.
class info(models.Model):
    name = models.CharField(max_length = 50)
    num = models.IntegerField()
    
def __str__(self):
    return self.name