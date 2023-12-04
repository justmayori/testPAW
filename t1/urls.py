from django.urls import path
from . import views

urlpatterns = [
    path('cat/', views.data_view, name='data_view'),
]
