from django import forms
from .models import Patient


class PatientForm(forms.ModelForm):
    last_menstrual_date = forms.DateField(required=True,
                                          widget=forms.DateInput(format=('%yy-%m-%d'),
                                                                 attrs={'type': 'date',}))
    class Meta:
        model = Patient
        fields = [
            'anc_number',
            'patient_name',
            'national_id',
            'patient_contact',
            'last_menstrual_date',
            'discharged',
        ]
