from django.db import models

# Create your models here.
class CreateBetLotto(models.Model):
    numberLotto = models.IntegerField()
    top = models.BooleanField(default=False,null=False,blank=False)
    down = models.BooleanField(default=False,null=False,blank=False)
    price = models.IntegerField()

class Employee(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)