from django.contrib import admin
from .models import Patient, Discharge
from .forms import PatientForm, DischargeForm  # WeightForm, BPForm, NoteForm, WeekForm,  SignUpForm


class PatientAdmin(admin.ModelAdmin):
    list_display = ('anc_number', 'patient_name', 'last_menstrual_date', 'patient_contact',)
    list_display_links = ('patient_name',)
    list_editable = ('patient_contact',)
    list_per_page = (6)
    search_fields = ('patient_name', 'anc_number',)
    form = PatientForm


admin.site.register(Patient, PatientAdmin)


class DischargeAdmin(admin.ModelAdmin):
    list_display = ('discharged','patient',)
    list_display_links = ('patient',)
    form = DischargeForm

admin.site.register(Discharge, DischargeAdmin )
