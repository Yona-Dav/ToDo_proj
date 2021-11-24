from django import forms
from .models import Category

class ToDoForm(forms.Form):
    title = forms.CharField(max_length=40)
    details = forms.CharField(max_length=300)
    deadline_date = forms.DateTimeField(widget=forms.TextInput(attrs={'placeholder': 'yyyy-mm-dd h:m:s'}))
    category = forms.ModelChoiceField(queryset=Category.objects.all())