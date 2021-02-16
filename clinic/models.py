from django.db import models

# Create your models here.
class CreateBetLotto(models.Model):
    numberLotto = models.IntegerField()
    top = models.BooleanField(default=False,null=False,blank=False)
    down = models.BooleanField(default=False,null=False,blank=False)
    price = models.IntegerField()
