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
            response = []
            userGoalObj = get_object_or_404(Activity, pk=request.GET['user'])
            userProgressObj = get_object_or_404(Progress, pk=request.GET['user'])
            resProgress = {}
            resGoal = {}
            resProgress['user'] = request.GET['user']
            resProgress['running'] = userProgressObj.running
            resProgress['sitting'] = userProgressObj.sitting
            resProgress['standing'] = userProgressObj.standing
            resProgress['lyingDown'] = userProgressObj.lyingDown
            resProgress['walking'] = userProgressObj.walking
            resGoal['user'] = request.GET['user']
            resGoal['running'] = userGoalObj.running
            resGoal['sitting'] = userGoalObj.sitting
            resGoal['standing'] = userGoalObj.standing
            resGoal['lyingDown'] = userGoalObj.lyingDown
            resGoal['walking'] = userGoalObj.walking
            response.append(resGoal)
            response.append(resProgress)
            return JsonResponse(response, safe=False)
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


@csrf_exempt
def updateProgress(request):
    if request.method == "POST":
        json_data = json.loads(request.body)
        label = json_data['label_names']
        pred = json_data['label_probs']
        label_pred = zip(pred, label)
        label_pred.sort(reverse=True)
        print label_pred[:10]
        label_set = [x[1] for x in label_pred[:10]]
        userProgressObj = get_object_or_404(Progress, pk="admin")
        if "Running" in label_set:
            print "update running   ",
            userProgressObj.running += 1

        if "Walking" in label_set:
            print "update walking   ",
            userProgressObj.walking += 1

        if "Lying down" in label_set:
            print "update lying   ",
            userProgressObj.lyingDown += 1

        if "Sitting" in label_set:
            print "update sitting   ",
            userProgressObj.sitting += 1

        if "Standing" in label_set:
            print "update standing    ",
            userProgressObj.standing += 1
        userProgressObj.save()
        print " "
        return HttpResponse("Updated activity")
