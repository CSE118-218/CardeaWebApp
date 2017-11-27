# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.serializers import json
from django.shortcuts import render, get_object_or_404
from django.utils.datastructures import MultiValueDictKeyError
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
import json
from patients.models import Activity, Progress
# Create your views here.
from django.http import HttpResponse, HttpResponseServerError, JsonResponse


def getAllActivity(request):
    return HttpResponse("get all activity")


@csrf_exempt
def goalActivity(request):
    if request.method == 'GET':
        try:
            userObj = get_object_or_404(Activity, pk=request.GET['user'])
            res = {}
            res['user'] = request.GET['user']
            res['running'] = userObj.running
            res['sitting'] = userObj.sitting
            res['standing'] = userObj.standing
            res['lyingDown'] = userObj.lyingDown
            res['walking'] = userObj.walking
            return JsonResponse(res)
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
            print userObj.running
            userObj.running += runningTime
            userObj.sitting += sittingTime
            userObj.standing += standingTime
            userObj.lyingDown += lyingDownTime
            userObj.walking += walkingTime
            userObj.save()
        except KeyError:
            return HttpResponseServerError("Malformed data!")
        return HttpResponse("Updated activity")


@csrf_exempt
def progressActivity(request):
    if request.method == 'GET':
        try:
            userObj = get_object_or_404(Progress, pk=request.GET['user'])
            res = {}
            res['user'] = request.GET['user']
            res['running'] = userObj.running
            res['sitting'] = userObj.sitting
            res['standing'] = userObj.standing
            res['lyingDown'] = userObj.lyingDown
            res['walking'] = userObj.walking
            return JsonResponse(res)
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
            userObj,created = Progress.objects.get_or_create(pk=user)
            print userObj.account, userObj.running
            userObj.running += runningTime
            userObj.sitting += sittingTime
            userObj.standing += standingTime
            userObj.lyingDown += lyingDownTime
            userObj.walking += walkingTime
            userObj.save()
        except KeyError:
            return HttpResponseServerError("Malformed data!")
        return HttpResponse("Updated activity")
