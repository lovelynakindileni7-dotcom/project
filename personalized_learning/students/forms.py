from django import forms
from .models import Performance

class PerformanceForm(forms.ModelForm):
    class Meta:
        model = Performance
        fields = ['G1', 'G2']

class StudentForm(forms.Form):
    age = forms.IntegerField(label='Age')
    study_time = forms.IntegerField(label='Study Time')
    failures = forms.IntegerField(label='Failures')
    absences = forms.IntegerField(label='Absences')
    G1 = forms.FloatField(label='First Test Score')
    G2 = forms.FloatField(label='Second Test Score')