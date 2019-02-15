from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.management import call_command
from django.http import HttpResponse,HttpRequest
from io import StringIO
from rank.forms import InputForm
import csv
import logging

count=0
reader = csv.DictReader(open('rank/sud_features.csv'))

def feature_extract(request):
	form = InputForm(request.POST)
	return render(request, 'rank_index.html', {'form':form})

def feature_display(request):
	form = InputForm(request.POST)

	result = {}
	for row in reader:
	    for column, value in row.items():
	        result.setdefault(column, value)
	print(result['nnz'])
	
	
	return render(request, 'rank_base_display.html', {'form':form,'result':result})

	
