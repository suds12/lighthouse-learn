from django import forms
from interface.models import LearningSet1
from django.forms import widgets




class DatasetForm(forms.Form):
	
	#choice_field = forms.ChoiceField(choices=random_forest_3.data['nedges'])
	choice=forms.ModelMultipleChoiceField(queryset=LearningSet1.objects.values_list('dataset'), widget=widgets.SelectMultiple(attrs={'size': 20}))
	#post=forms.CharField()