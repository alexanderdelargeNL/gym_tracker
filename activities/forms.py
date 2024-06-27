from django import forms
from .models import Activity, MuscleGroup, CardioExercise
import datetime

class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ['date', 'musclegroup', 'cardioexercise', 'duration', 'notes', 'is_rest']
        labels = {
            'date': 'Datum',
            'musclegroup': 'Spiergroep',
            'cardioexercise': 'Cardio-oefening',
            'duration': 'Duur (minuten)',
            'notes': 'Notitie',
            'is_rest': 'Rustdag',
        }        
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'musclegroup': forms.Select(attrs={'class': 'form-control'}),
            'cardioexercise': forms.Select(attrs={'class': 'form-control'}),
            'duration': forms.NumberInput(attrs={'class': 'form-control', 'value': 0}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'is_rest': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date'].initial = datetime.date.today()
