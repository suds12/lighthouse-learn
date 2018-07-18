from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.management import call_command
from django.http import HttpResponse,HttpRequest
from io import StringIO
from interface.learn_scripts.models import random_forest_3
from interface.models import LearningSet1
import json
#from interface.models import user_dp

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



def search_form(request):
    return render(request, 'bfs_search.html')

def search(request):
	if 'dp' in request.GET:
		message="you serched for: %r" % request.GET['dp']
	else:
		message="empty "
	return HttpResponse(message)

def bfs_response(request):
	dp = LearningSet1.objects.get(index=213)
	return render(request, 'bfs_response.html', 
		{'dataset': dp.dataset, 'package': dp.package, 'runtime':dp.runtime, 'classification':dp.classif, 'nedges':dp.nedges, 'nvertices':dp.nvertices, 'nthreads':dp.nthreads, 'nodes_in_largest_wcc':dp.nodes_in_largest_wcc, 'nodes_in_largest_scc':dp.nodes_in_largest_scc, 'edges_in_largest_wcc':dp.edges_in_largest_wcc, 'edges_in_largest_scc':dp.edges_in_largest_scc,'average_clustering_coefficient':dp.average_clustering_coefficient, 'number_of_triangles':dp.number_of_triangles, 'fraction_of_closed_triangles':dp.fraction_of_closed_triangles, 'diameter_longest_shortest_path_field':dp.diameter_longest_shortest_path_field})


		
		
