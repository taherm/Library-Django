from django import forms
from django.forms import extras
from books.models import BookIssue,Book
from members.models import Members

class BookIssueForm(forms.ModelForm):
	IssueId = forms.CharField(label='Book Issue ID')
	MemId = forms.ModelChoiceField(queryset=Members.objects.all())
	Book = forms.ModelChoiceField(queryset=Book.objects.all())
	IssueDate = forms.DateField(label='Issue Date',widget=extras.SelectDateWidget)
	ReturnDate = forms.DateField(label='Return Date',widget=extras.SelectDateWidget)

	class Meta:
		model = BookIssue
		fields = '__all__'