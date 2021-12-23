from django import forms
from .models import Printer

class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Printer
        fields = '__all__'
