# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here
class Listing(models.Model):
	username = models.CharField(max_length=50)
	first = models.CharField(max_length=150)
	last = models.CharField(max_length = 150)
	password = models.CharField(max_length=50)
	email = models.EmailField() 