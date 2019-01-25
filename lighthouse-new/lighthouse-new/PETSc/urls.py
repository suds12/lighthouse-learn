from django.conf.urls import url
from django.conf import settings
from PETSc import views


urlpatterns = [
    url(r'^$', views.petsc),
    url(r'^linear_system/$', views.linear_system),
    url(r'^linear_system/generateCode/$', views.petsc_code),
]