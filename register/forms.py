from django import forms
from .models import Patient  # Note, Weight, BP, SignUp, Week
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from django.forms.extras.widgets import SelectDateWidget


class PatientForm(forms.ModelForm):
    last_menstrual_date = forms.DateField(required=True,
                                          widget=forms.DateInput(format=('%yy-%m-%d'),
                                                                 attrs={'type': 'date',}))

    class Meta:
        model = Patient
        fields = [
            'uuid',
            'anc_number',
            'patient_name',
            'national_id',
            'patient_contact',
            'last_menstrual_date'
        ]  # class SignUpForm(forms.ModelForm):

# class Meta:
# 		model = SignUp
# 		fields= [
# 			'full_name',
# 			'password',
# 			'password2',
# 			'email',
# 		]
#
# class NoteForm(forms.ModelForm):
# 	class Meta:
# 		model = Note
# 		fields = [
# 			'patient',
# 			'service',
# 			'clinical_note',
# 		]
#
# class WeightForm(forms.ModelForm):
# 	class Meta:
# 		model = Weight
# 		fields = [
# 			'patient',
# 			'weight',
# 			'week',
# 		]
#
# class BPForm(forms.ModelForm):
# 	class Meta:
# 		model = BP
# 		fields = [
# 			'patient',
# 			'diastole',
# 			'systole',
# 			'week',
# 		]
#
# class WeekForm(forms.ModelForm):
# 	class Meta:
# 		model = Week
# 		fields = ['week',]
