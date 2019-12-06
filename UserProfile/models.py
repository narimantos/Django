# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UserProfile(models.Model):
    naam = models.CharField(max_length=512)
    achternaam = models.CharField(max_length=512)