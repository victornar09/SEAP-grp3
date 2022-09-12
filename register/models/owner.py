
import email
from xml.parsers.expat import model
from django.db import models

class owner (models.Model):
    idOwner = models.IntegerField('Owner', unique = True)
    nameOwner =  models.CharField('name-owner',max_length=100)
    addressOwner = models.CharField('address-owner',max_length=100)
    emailOwner = models.CharField('email-owner', max_length=100)
