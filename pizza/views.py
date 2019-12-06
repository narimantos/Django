# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
from .models import Pizza
def index(request, pid):
    pizza = Pizza.objects.get(id=pid)
    return HttpResponse(
        content={
            'id': pizza.id,
            'title': pizza.title,
            'description': pizza.description,
        }
    )
# Create your views here.
