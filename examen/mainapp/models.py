# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, ValidationError
from django.db.models import Sum
# Create your models here.
class Customer (models.Model):
    user = models.OneToOneField(User,default=None)
    
    def __str__(self):
        return self.user.username

class Product(models.Model):
    name = models.CharField('name',max_length=55)
    price = models.IntegerField('price')
    stock = models.IntegerField('stock')
    users = models.ManyToManyField(Customer,
    through="CustProd")


class CustProd(models.Model):
    product = models.ForeignKey(Product)
    customer = models.ForeignKey(Customer)
    class Meta:
        unique_together = ('product','customer')

