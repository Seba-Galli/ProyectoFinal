from django import forms

class Estac_Form(forms.Form):
    PrecioHora=forms.FloatField()
    hora_ingreso=forms.DateTimeField()
    hora_egreso=forms.DateTimeField()