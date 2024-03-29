"""Forms of the project."""
from django import forms
from .models import Thing

class ThingForm(forms.ModelForm):
    class Meta:
        model = Thing
        fields = ['name', 'description', 'quantity']
        widgets = {'description': forms.Textarea(attrs={'cols': 40, 'rows': 5}), 'quantity': forms.NumberInput()}
# Create your forms here.
