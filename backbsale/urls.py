from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404
from . import views

urlpatterns = [
    path('', views.index, name='inicio'),
    path('api/v0/', include('api_rest.urls'))
]

handler404 = 'api_rest.views.mi_error_404'
