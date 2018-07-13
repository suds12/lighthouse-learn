from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.management import call_command
from django.http import HttpResponse,HttpRequest
from io import StringIO


# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

class BFSPageView(TemplateView):
	template_name="BFS.html"
	


def bfs(request):
		# out = StringIO()
		# call_command('run_bfs', stdout=out)
		# value = out.getvalue()
		# print("result:")
		# print(value)
		# return HttpResponse(value)
		a=call_command('run_bfs')
		return HttpResponse(a)

		
		