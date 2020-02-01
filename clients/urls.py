from django.urls import path
from . import views
from .models import Client
from .views import (
    ClientListView,
    ClientUpdateView,
    ClientDetailView,
    ClientDeleteView,
    ClientCreateView,
    Comment,
)


urlpatterns = [

    path('<int:pk>/edit/',
         ClientUpdateView.as_view(), name='client_edit'),
    path('<int:pk>/',
         ClientDetailView.as_view(), name='client_detail'),
    path('<int:pk>/delete/',
         ClientDeleteView.as_view(), name='client_delete'),
    path('new/', ClientCreateView.as_view(), name='client_new'),
    path('', ClientListView.as_view(), name='client_list'),

]
