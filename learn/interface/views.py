from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.management import call_command
from django.http import HttpResponse,HttpRequest
from io import StringIO
from interface.learn_scripts.models import random_forest_3
from interface.models import LearningSet1
from interface.forms import DatasetForm
import json
import matplotlib.pyplot as plt
import numpy as np
import pickle
import logging
logging.basicConfig(filename='example.log', filemode='w', level=logging.DEBUG)


# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

class BFSPageView(TemplateView):
	template_name="BFS.html"
	


def bfs(request):
	datafile="interface/learn_scripts/datasets/classifier_bfs.csv"
	random_forest_3.main(datafile)
	var=random_forest_3.json_data
	return HttpResponse(var['m'])



def search_form(request):									#Outer form for entering features
    return render(request, 'bfs_search.html')

def search(request):										#Redirects to this page for rendering ML result
	if 'dp' in request.GET:
		message="you serched for: %r" % request.GET['dp']
	else:
		message="empty "
	return HttpResponse(message)

def bfs_response(request):
	dp = LearningSet1.objects.get(index=213)
	return render(request, 'bfs_response.html', 
		{'dataset': dp.dataset, 'package': dp.package, 'runtime':dp.runtime, 'classification':dp.classif, 'nedges':dp.nedges, 'nvertices':dp.nvertices, 'nthreads':dp.nthreads, 'nodes_in_largest_wcc':dp.nodes_in_largest_wcc, 'nodes_in_largest_scc':dp.nodes_in_largest_scc, 'edges_in_largest_wcc':dp.edges_in_largest_wcc, 'edges_in_largest_scc':dp.edges_in_largest_scc,'average_clustering_coefficient':dp.average_clustering_coefficient, 'number_of_triangles':dp.number_of_triangles, 'fraction_of_closed_triangles':dp.fraction_of_closed_triangles, 'diameter_longest_shortest_path_field':dp.diameter_longest_shortest_path_field, 'x90_percentile_effective_diameter':dp.x90_percentile_effective_diameter})


def dataset_form(request): 
	form=DatasetForm()  
	return render(request, 'dataset_form_template.html', {'form':form})

	

def custom_bfs(request):
	form=DatasetForm(request.GET)
	selected=request.GET.get('choice')		
	selected=selected.strip("[]")			#preprocessing
	selected=selected.strip("''")
	logging.info(selected)



	# if form.is_valid():
	# 	message = form.cleaned_data['post']
	# 	logging.info('ans is %s',message)
	# 	#print(message)
	# else:
	# 	print("bns")

	# args={'form': form, 'message': message}
	# return render(request, 'dataset_form_template.html', args)
	global dp
	dp = LearningSet1.objects.get(dataset=selected, package='GraphMat')
	#ax = plt.subplot(111)

	return render(request, 'bfs_response.html', 
		{'dataset': dp.dataset, 'package': dp.package, 'runtime':dp.runtime, 'classification':dp.classif, 'nedges':dp.nedges, 'nvertices':dp.nvertices, 'nthreads':dp.nthreads, 'nodes_in_largest_wcc':dp.nodes_in_largest_wcc, 'nodes_in_largest_scc':dp.nodes_in_largest_scc, 'edges_in_largest_wcc':dp.edges_in_largest_wcc, 'edges_in_largest_scc':dp.edges_in_largest_scc,'average_clustering_coefficient':dp.average_clustering_coefficient, 'number_of_triangles':dp.number_of_triangles, 'fraction_of_closed_triangles':dp.fraction_of_closed_triangles, 'diameter_longest_shortest_path_field':dp.diameter_longest_shortest_path_field, 'x90_percentile_effective_diameter':dp.x90_percentile_effective_diameter})
	

def visualize(request):
	x = np.linspace(0, 10)
	y = np.exp(x)
	plt.plot(x, y)
	fig = plt.gcf()
	fig.savefig('fig1.png')
	#plt.show()
	image_data = open("fig1.png", "rb").read()
	return HttpResponse(image_data, content_type="image/png")

		
		
