from django.db import models

# Create your models here.
class CreateBet(models.Model):
    numberLotto = models.IntegerField()
    top = models.BooleanField()
    down = models.BooleanField()
    price = models.IntegerField()
