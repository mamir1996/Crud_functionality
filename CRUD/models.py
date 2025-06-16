from django.db import models

# Create your models here.
class Registration(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    roll_num=models.IntegerField(null=True)
    subject=models.CharField(max_length=100)