from django.urls import path
from .views import data_view

urlpatterns = [
    path('', data_view, name='data_view'),
]