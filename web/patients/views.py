# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.serializers import json
from django.shortcuts import render, get_object_or_404
from django.utils.datastructures import MultiValueDictKeyError
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
import json
from patients.models import Activity
# Create your views here.
from django.http import HttpResponse, HttpResponseServerError


def getAllActivity(request):
    return HttpResponse("get all activity")


@csrf_exempt
def goalActivity(request):
    if request.method == 'GET':
        try:
            print request.GET['activity']
        except MultiValueDictKeyError:
            return HttpResponse("no such key")
    if request.method == "POST":
        json_data = json.loads(request.body)
        try:
            user = json_data['user']
            walkingTime = json_data["walking"]
            runningTime = json_data["running"]
            sittingTime = json_data["sitting"]
            standingTime = json_data["standing"]
            lyingDownTime = json_data["lyingDown"]
            userObj = get_object_or_404(Activity, pk=user)
            if not userObj:
                print "user not exit"
            else:
                print "get usr"

            print walkingTime, runningTime, sittingTime, standingTime, lyingDownTime
        except KeyError:
            return HttpResponseServerError("Malformed data!")
        return HttpResponse("Updated activity")


