from django import forms
from services.models import Service

class ServiceForm(forms.ModelForm):
	class Meta:
		model = Service
		fields = [
            'id',
			'service_name',
            'service_about',
			'service_url',
            'service_msg',
		]
