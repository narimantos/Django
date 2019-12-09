# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Pizza
class PizzaAdmin(admin.ModelAdmin):
    pass

admin.site.register(Pizza, PizzaAdmin)