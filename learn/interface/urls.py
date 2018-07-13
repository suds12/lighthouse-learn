from django.conf.urls import url
from interface import views

urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^BFS/$', views.bfs),
]
