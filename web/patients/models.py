# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Patients(models.Model):
    account = models.CharField(max_length=20, default="")
    password = models.CharField(max_length=20, default="")
    name = models.CharField(max_length=40, default="")
    age = models.IntegerField(default=0)
    pass


class Activity(models.Model):
    patientID = models.ForeignKey('Patients',on_delete=models.CASCADE, primary_key= True)
    category = models.CharField(max_length=30, primary_key=True)
    start_time = models.DateTimeField(auto_now=False, primary_key=True)
    end_time = models.DateTimeField(auto_now=False)
    duration = models.DateTimeField()
    pass