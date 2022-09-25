

from django.db import models
from .owner import owner

class property (models.Model):
    
    idProperty = models.BigAutoField(primary_key=True,blank=False, null=False)
    addressProperty = models.CharField('addressProperty', max_length=100, unique= True, blank=False, null=False)
    idOwner = models.ForeignKey(owner,related_name='property',on_delete=models.CASCADE, blank=False, null=False)
    typeProperty = models.IntegerField('type',blank=False, null=False)

    class Meta: 
        verbose_name = 'property'
        verbose_name_plural = 'propertys'

        def __str__(self):
            return self.addressProperty 
    