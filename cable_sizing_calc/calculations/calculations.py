import math

#Calculates full load current. Takes in power[kW], voltage [V], power factor [0-1]
def fullLoadCurrent(kW, v, pf):
    return round(((kW * 1000)/(math.sqrt(3) * v * pf)),2)

#Calculate volt drop as a % of the rated voltage
def voltage_drop(impedance_m, voltage, current, d):
    return round((impedance_m * current * (d / 1000))/voltage * 100,2)

def short_circuit_kA(t, cable):
    k = select_k(cable)
    return round(((cable.cross_section * k)/math.sqrt(t))/1000, 2)

def select_k(cable):
    k = {'copper': {'PVC':115, 'XLPE': 143, 'PILC': 115},
         'aluminium': {'PVC':76, 'XLPE': 92, 'PILC': 76}}
    return k.get(cable.conductor).get(cable.insulation)
