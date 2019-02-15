from django import forms

matvec_choices = (
	(0,	'Matrix vector multiplication'),
	(1,	'Memory access'),
)

class InputForm(forms.Form):
	matrix_file = forms.FileField( label='Select matrix file for upload.')
	# output_file = forms.CharField(label="Please enter the output file to append results to.")
	interior_points = forms.FloatField(label='Please enter percentage of rows to sample as interior points(0,1)')
	pmax = forms.IntegerField(label='max number of rows to sample in a matrix ( -1 == no maximum )')
	edge_points = forms.FloatField(label='Please enter percentage of rows to sample as edge points(0,1)')
	matvec = forms.ChoiceField(choices=matvec_choices, widget=forms.RadioSelect(), label='How do you want to get values?')


