from django import forms
from .models import Printer, MeterReading


class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Printer
        fields = '__all__'


class MeterReadingForm(forms.ModelForm):
    class Meta:
        model = MeterReading
        fields = ['date', 'meter_location', 'reading']





