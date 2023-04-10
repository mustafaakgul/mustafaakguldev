from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
	class Meta:
		model = Contact

		fields = [
			'name',
			'email',
			'phone',
            'subject',
            'message',
		]

		# widgets = {
		# 	'case_name': forms.TextInput(attrs={'class': 'form-control'}),
		# 	'initial_balance': forms.NumberInput(attrs={'class': 'form-control'}),
		# 	'case_date' : forms.DateInput(format = '%Y-%m-%d', attrs={'type' : 'date', 'class': 'form-control'}),
		# }