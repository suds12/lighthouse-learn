from django.conf.urls import url
from django.conf import settings
from rank import views


urlpatterns = [
	url(r'^$', views.feature_extract),
	url(r'^display/$', views.feature_display),
]