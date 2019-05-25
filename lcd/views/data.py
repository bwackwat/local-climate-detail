from datetime import datetime, timedelta
import json

from django.shortcuts import render, redirect
from django import forms
from django.contrib.auth.decorators import login_required

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
    location = SensorLocation.objects.filter(pk=request.GET.get('location'))
    if location is None:
        raise SensorLocation.DoesNotExist

    end_date = date.today()
    start_date = end_date - timedelta(days=1)
    data = ClimateData.objects.filter(location=location, date__range=[start_date, end_date])
    
    return HttpResponse(json.dumps(data), content_type='application/json')
