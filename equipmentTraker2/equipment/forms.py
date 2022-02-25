#!/usr/bin/env python3
from .models import equipment
from django import forms


class equipmentForm(forms.ModelForm):

    class Meta:
        bu = [('KIU', 'KIU'), ('SIU', 'SIU'), ('AGU', 'AGU'), ('NAU', 'NAU'), ('ADU', 'ADU')]
        bl = [('SWT', 'SWT'), ('SLS', 'SLS'), ('WHM', 'WHM'), ('DST', 'DST')]
        model = equipment
        fields = '__all__'
        widgets = {
            'description': forms.Textarea(attrs={'rows': 2}),
            'BU': forms.Select(choices=bu),
            'BL': forms.Select(choices=bl),
        }
