from django.db import models
from .owner import owner

class property (models.Model):
    idProperty = models.BigAutoField(primary_key=True)
    addressProperty = models.CharField('addressProperty', max_length=100, unique= True)
    idOwner = models.ForeignKey(owner,related_name='property',on_delete=models.CASCADE)
    typeProperty = models.IntegerField('type')
    