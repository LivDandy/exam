from __future__ import unicode_literals

from django.db import models
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.

class UserManager(models.Manager):
    def basic_validator(self, postData):
        print(postData)
        errors = {}
        if len(postData['first_name']) < 5:
            errors["first_name"] = "First name should be more than 5 characters"
        if len(postData['last_name']) < 5:
            errors["last_name"] = "Last name should be more than 5 characters"
        if not EMAIL_REGEX.match(postData['email']):
            errors["email"] = "Email must be valid!"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()