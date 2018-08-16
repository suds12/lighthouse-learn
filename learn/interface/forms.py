from django import forms
from interface.models import LearningSet1
from interface.models import Input
from django.forms import widgets




class DatasetForm(forms.Form):
	
	#choice_field = forms.ChoiceField(choices=random_forest_3.data['nedges'])
	choice=forms.ModelMultipleChoiceField(queryset=LearningSet1.objects.values_list('dataset'), widget=widgets.SelectMultiple(attrs={'size': 20}))
	#post=forms.CharField()

class SelectForm(forms.ModelForm):
	dataset_list=LearningSet1.objects.values_list('dataset')
	#dataset=forms.ModelMultipleChoiceField(queryset=LearningSet1.objects.values_list('dataset'), widget=widgets.SelectMultiple(attrs={'size': 20}))
	dataset = forms.ModelChoiceField(queryset=LearningSet1.objects.order_by('dataset').values_list('dataset'))
	#name = forms.CharField(max_length=128, help_text="Please enter the category name.")
	# views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
	# likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
	# slug = forms.CharField(widget=forms.HiddenInput(), required=False)

	# An inline class to provide additional information on the form.
	class Meta:
	    # Provide an association between the ModelForm and a model
	    model = Input
	    fields = ('dataset',)