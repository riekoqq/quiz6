from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name="routes"),
    path('drugs/', views.getDrugs, name="drugs"),
    path('drugs/<str:pk>', views.getDrug, name="drug"),
]