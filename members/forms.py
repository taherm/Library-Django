from django import forms
from django.forms import extras
from members.models import Members

class Memberform(forms.ModelForm):
	mem_id = forms.IntegerField(label='Member ID')
	mem_name = forms.CharField(label='Member Name')
	mem_addr = forms.CharField(label='Member Address')
	mem_reg = forms.DateField(label='Registration Date',widget=extras.SelectDateWidget)
	mem_exp = forms.DateField(label='Expiry Date',widget=extras.SelectDateWidget)

	class Meta:
		model = Members
		fields = '__all__'