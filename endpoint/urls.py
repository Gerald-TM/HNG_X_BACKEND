from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_endpoint_view, name='get_enpoint')
]