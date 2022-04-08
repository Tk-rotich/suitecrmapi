from django import forms
from suiterest import validators

class StartDateForm(forms.Form):
    start_date = forms.DateField(
        validators =[validators.future_dates],
        input_formats=['%Y-%m-%d'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datepicker',
            'data-target': '#datetimepicker1',
            'type': 'date'
        })
    )