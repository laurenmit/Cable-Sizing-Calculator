from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CableForm, CalculationForm
from .models import Cable
import math

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

def cable_info(request):
    if request.method == "POST":
        form = CableForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("details")
    else:
        form = CableForm()
    return render(request, 'calculations/cables.html', {'form': form})


def calculate(request):
    if request.method == "POST":
        form = CableForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("welcome")
    else:
        form = CalculationForm()
    return render(request, 'calculations/calculate.html', {'form': form})


#Calculates full load current. Takes in power[kW], voltage [V], power factor [0-1]
def fullLoadCurrent(kW, V, pf):
    return (kW/(math.sqrt(3)*V*pf))


def cable_detail(request):
    cables = Cable.objects.all()
    return render(request, 'calculations/cable_detail.html', {"cables": cables})
