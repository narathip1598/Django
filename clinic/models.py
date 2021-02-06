from django.db import models

# Create your models here.
class CreateBetLotto(models.Model):
    numberLotto = models.IntegerField()
    top = models.BooleanField(default=False)
    down = models.BooleanField(default=False)
    price = models.IntegerField()