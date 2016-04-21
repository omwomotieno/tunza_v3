from django import forms
from services.models import Service

class ServiceForm(forms.ModelForm):
	class Meta:
		model = Service
		fields = [
			'service_name',
            'service_about',
			'service_url',
            'service_file',
		]
