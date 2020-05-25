import math

#Calculates full load current. Takes in power[kW], voltage [V], power factor [0-1]
def fullLoadCurrent(kW, V, pf):
    return round((kW/(math.sqrt(3)*V*pf)),2)

#Calculate volt drop as a % of the rated voltage
def voltage_drop(impedance_m, voltage, current, d):
    return round((impedance_m * current * d)/voltage * 100,2)
