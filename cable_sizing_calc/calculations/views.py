from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CableForm, CalculationForm
from .models import Cable
from . import calculations as calc


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
        form = CalculationForm(request.POST)
        if form.is_valid():
            id = request.POST.get('choose_cable')
            cable = Cable.objects.get(pk=id)
            power = form.cleaned_data.get('power')
            pf = form.cleaned_data.get('power_factor')
            voltage = form.cleaned_data.get('voltage')
            distance = form.cleaned_data.get('distance')
            time = form.cleaned_data.get('time')
            current = calc.fullLoadCurrent(power, voltage, pf)
            impedance_m = cable.impedance
            v_drop = calc.voltage_drop(impedance_m, voltage, current, distance)
            short_circuit_current = calc.short_circuit_kA(time, cable) 
            if v_drop < 5:
                v_limit = False
            else:
                v_limit = True
            return render(request, 'calculations/results.html',
                          {'power': power,
                           'pf':pf,
                           'voltage': voltage,
                           'distance': distance,
                           'current': current,
                           'v_drop': v_drop,
                           'v_limit': v_limit,
                           'short_circuit': short_circuit_current
                           })
    else:
        cables = Cable.objects.all()
        form = CalculationForm()
    return render(request, 'calculations/calculate.html', {'form': form, 'cables': cables})

def delete(request, id):
    Cable.objects.get(pk=id).delete()
    return redirect("details")

def results(request, power):
    pf = 1
    voltage = 10
    distance = 100
    current = 60
    return render(request, 'calculations/results.html', {'power': power, 'pf':pf,
                    'voltage': voltage, 'distance':distance, 'current': current})

def cable_detail(request):
    cables = Cable.objects.all()
    return render(request, 'calculations/cable_detail.html', {"cables": cables})
