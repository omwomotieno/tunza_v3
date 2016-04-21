from django import forms
from .models import Reminder


class ReminderForm(forms.ModelForm):
    appointment_date = forms.DateField(label="Date of Reminder", required=True,
                                    widget=forms.DateInput(format=('%y-%m-%d'),
                                                           attrs={'type': 'date',}))
    time_of_call = forms.TimeField(label="Time of Call", required=True,
                                    widget=forms.TimeInput(format=('%I:%M'),
                                                           attrs={'type': 'time',}))
    class Meta:
        model = Reminder
        fields = [
            'patient', 'service', 'appointment_date', 'time_of_call',
            'response',
        ]
