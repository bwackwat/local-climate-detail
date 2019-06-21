from datetime import datetime, timedelta, date
import json
import sys

from django.shortcuts import render, redirect
from django import forms
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Min, Max

from lcd.models import *


@login_required
def set_current_location(request):
    if request.user.is_superuser and request.method == 'POST':
        new_location = SensorLocation.objects.filter(pk=request.POST['location'])
        if new_location is None:
            raise SensorLocation.DoesNotExist
        
        locations = SensorLocation.objects.all().update(current=False)
        for location in locations:
            location.save()

        new_location.current = True
        new_location.save()
    return redirect('home')


@login_required
def create_location(request):
    if request.user.is_superuser and request.method == 'POST':
        SensorLocation(description=request.POST['description']).save()
    return redirect('home')


def get_data(request):
    location = SensorLocation.objects.filter(pk=request.GET.get('location')).first()
    if location is None:
        location = SensorLocation.objects.filter(current=True).first()


    if request.GET.get('end_date'):
        print(request.GET.get('end_date'), file=sys.stderr)
        end_date = datetime.strptime(request.GET.get('end_date'), '%a, %d %b %Y %H:%M:%S %Z')
        print(end_date, file=sys.stderr)
    else:
        end_date = date.today()

    if request.GET.get('start_date'):
        start_date = datetime.strptime(request.GET.get('start_date'), '%a, %d %b %Y %H:%M:%S %Z')
    else:
        start_date = end_date - timedelta(days=1)
    
    climate_data = ClimateData.objects.filter(location=location, date__range=[start_date, end_date])

    return JsonResponse({
        "data": list(climate_data.values())
        #"min_temperature": climate_data.aggregate(Min('temperature'))['temperature__min'],
        #"max_temperature": climate_data.aggregate(Max('temperature'))['temperature__max']
    })
