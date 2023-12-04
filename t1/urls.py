from django.urls import path
from .views import data_view

urlpatterns = [
    path('cat/', views.data_view, name='data_view'),
]
