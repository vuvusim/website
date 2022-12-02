from django.urls import path, include
from . import views

urlpatterns = [
    path('projects/', views.projects),
    path('project/<str:pk>/', views.project),
]