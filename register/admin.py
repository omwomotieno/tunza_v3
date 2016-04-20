from django.contrib import admin
from .models import Patient
from .forms import PatientForm #WeightForm, BPForm, NoteForm, WeekForm,  SignUpForm

class PatientAdmin(admin.ModelAdmin):
	list_display = ('anc_number', 'patient_name', 'last_menstrual_date', 'active', 'patient_contact')
	list_display_links = ('patient_name',)
	list_editable = ('patient_contact', 'active',)
	list_per_page = (6)
	search_fields = ('patient_name', 'anc_number',)
	form = PatientForm

admin.site.register(Patient, PatientAdmin)

#
# class WeightAdmin(admin.ModelAdmin):
# 	list_display = ('weight', 'date_of_input', 'week', 'patient',)
# 	list_display_links = ('patient',)
# 	list_per_page = (6)
# 	search_fields = ('patient',)
# 	form = WeightForm
#
#
# class BPAdmin(admin.ModelAdmin):
# 	list_display = ('diastole', 'systole', 'date_of_input', 'week', 'patient',)
# 	list_display_links = ('patient',)
# 	list_per_page = (6)
# 	search_fields = ('patient',)
# 	form = BPForm
#
#
# class NoteAdmin(admin.ModelAdmin):
# 	list_display = ['patient', 'service', 'clinical_note', 'date_created', ]
# 	list_display_links = ('patient',)
# 	list_per_page = (6)
# 	search_fields = ('patient',)
# 	form = NoteForm
#
#
# class WeekAdmin(admin.ModelAdmin):
# 	list_display = ['week', ]
# 	form = WeekForm

# class SignUpAdmin(admin.ModelAdmin):
# 	list_display = ['full_name', 'email']
# 	form = SignUpForm

# admin.site.register(SignUp, SignUpAdmin)

# admin.site.register(Weight, WeightAdmin)
# admin.site.register(BP, BPAdmin)
# admin.site.register(Note, NoteAdmin)
