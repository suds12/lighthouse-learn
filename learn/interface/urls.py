from django.conf.urls import url
from interface import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^BFS/$', views.bfs_response),
    url(r'^search-request/$', views.search_form),
    url(r'^search/$', views.search),
    url(r'^bfs-response/$', views.bfs_response),
    url(r'^run/$', views.bfs),
    url(r'^select-dataset/$', views.dataset_form),
    url(r'^custom-bfs/$', views.custom_bfs),
    url(r'^visualize/$', views.visualize),
]
