from __future__ import unicode_literals
import re
from django.db import models

EMAIL_REGEX=re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

class UserManager(models.Manager):
    def validate(self,post_data):
        errors={}
        for field,value in post_data.iteritems():
            if len(value)<1:
                errors[field]="{} field is required".format(field.replace('_',''))
            if field == "first_name" or field =="last_name":
                if not field in errors and len(value) < 3:
                    errors[field]="{} field must be at least 3 characters".format(field.replace('_',''))
        if not "email" in errors and not re.match(EMAIL_REGEX, post_data['email']):
            errors['email']="Invalid Email"
        else:
            if len(self.filter(email=post_data['email']))> 1:
                errors['email']= "Email is already in use"
        return errors

class User(models.Model):
    first_name= models.CharField(max_length=255)
    last_name= models.CharField(max_length=255)
    email= models.CharField(max_length=255)
    password= models.CharField(max_length=255)
    created_at= models.DateTimeField(auto_now_add=True)
    updated_at= models.DateTimeField(auto_now=True)
    objects = UserManager()

class Address(models.Model):
    street=models.CharField(max_length=255)
    city= models.CharField(max_length=255)
    state= models.CharField(max_length=2)
    zipcode= models.IntegerField(max_length=5)
    mailing_user_id= models.ManyToManyField(User, related_name="mailing_address_id", null=True)
    shipping_user_id= models.ManyToManyField(User, related_name="shipping_address_id", null=True)

class Order(models.Model):
    users=models.ForeignKey(User, related_name="orders", null=True)

class Product(models.Model):
    name= models.CharField(max_length=255)
    desc= models.TextField(null=True)
    orders= models.ForeignKey(Order, related_name="products", null=True)

# Create your models here.
