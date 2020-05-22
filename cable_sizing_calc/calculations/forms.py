from django import forms
from .models import Cable

cross_sect_choices = [
    (1.5, '1.5mm\u00b2'),
    (2.5, '2.5mm\u00b2'),
    (4, '4mm\u00b2'),
    (6, '6mm\u00b2'),
    (10, '10mm\u00b2'),
    (16, '16mm\u00b2'),
    (25, '25mm\u00b2'),
    (35, '35mm\u00b2'),
    (50, '50mm\u00b2'),
    (70, '70mm\u00b2'),
    (95, '95mm\u00b2'),
    (120, '120mm\u00b2'),
    (150, '150mm\u00b2'),
    (185, '185mm\u00b2'),
    (240, '240mm\u00b2'),
    (300, '300mm\u00b2'),
]

insul_choices = [
    ('PVC', 'PVC'), #(actual, human readable)
    ('XLPE','XLPE'),
    ('PILC', 'PILC'),
]

cond_choices = [
    ('copper', 'Copper'),
    ('aluminium', 'Aluminium')
]

volt_rate_choices = [
    ('600/1000 V', '600/1000 V'),
    ('6.35/11 kV', '6.35/11 kV')
]

class CableForm(forms.ModelForm):
    cross_section = forms.FloatField(widget=forms.Select(choices=cross_sect_choices))
    nom_current_rating = forms.IntegerField() #unit is [A]
    conductor = forms.CharField(max_length=15, widget=forms.Select(choices=cond_choices))
    insulation = forms.CharField(max_length=5, widget=forms.Select(choices=insul_choices))
    voltage_rating = forms.CharField(max_length=20, widget=forms.Select(choices=volt_rate_choices))
    short_circuit_1s = forms.FloatField() # unit is [kA]
    impedance = forms.FloatField()

    def __init__(self, *args, **kwargs):
         super(forms.ModelForm, self).__init__(*args, **kwargs)
         self.fields['nom_current_rating'].label = 'Current Rating'

    class Meta:
         model = Cable
         fields = (
                     'cross_section',
                     'nom_current_rating',
                     'conductor',
                     'insulation',
                     'voltage_rating',
                     'short_circuit_1s',
                     'impedance',
                 )


class CalculationForm(forms.Form):
    power = forms.FloatField() #unit is [kW]
    voltage = forms.IntegerField(min_value=0) #unit is [A]
    power_factor = forms.FloatField(min_value=-1.0, max_value=1.0)
    distance = forms.FloatField(min_value=0.0) #unit is [m]
