from datetime import date
from django import forms

def future_dates(start_date):
  if start_date >= date.today():
    raise forms.ValidationError("Invalid date(Start date should be past date)")