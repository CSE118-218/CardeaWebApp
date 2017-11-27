# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Patients(models.Model):
    account = models.CharField(max_length=20, default="", primary_key=True)
    password = models.CharField(max_length=20, default="")
    name = models.CharField(max_length=40, default="")
    age = models.IntegerField(default=0)


class Activity(models.Model):
    account = models.OneToOneField(
        Patients,
        on_delete=models.CASCADE,
        primary_key=True,
        default="",
    )
    running = models.FloatField(default=0.0)
    sitting = models.FloatField(default=0.0)
    standing = models.FloatField(default=0.0)
    walking = models.FloatField(default=0.0)
    lyingDown = models.FloatField(default=0.0)
    # act = Activity(running=5.2, sitting=3.2, standing=4.2, walking=14.1, lyingDown=4.1, )


class Progress(models.Model):
    account = models.OneToOneField(
        Patients,
        on_delete=models.CASCADE,
        primary_key=True,
        default="",
    )
    running = models.FloatField(default=0.0)
    sitting = models.FloatField(default=0.0)
    standing = models.FloatField(default=0.0)
    walking = models.FloatField(default=0.0)
    lyingDown = models.FloatField(default=0.0)
    # act = Activity(running=5.2, sitting=3.2, standing=4.2, walking=14.1, lyingDown=4.1, )
