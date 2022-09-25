
from django.db import models

class owner (models.Model):
    idOwner = models.IntegerField('Owner', unique = True, blank=False, null=False)
    nameOwner =  models.CharField('name-owner',max_length=100, blank=False, null=False)
    addressOwner = models.CharField('address-owner',max_length=100, blank=False, null=False)
    emailOwner = models.CharField('email-owner', max_length=100, blank=False, null=False)

    class Meta: 
        verbose_name = 'owner'
        verbose_name_plural = 'owners'

        def __str__(self):
            return self.nameOwner

