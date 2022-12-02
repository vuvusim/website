from django.shortcuts import render
from .models import Project

def projects(request):
    return render(request, 'projects/projects.html')

def project(request, pk):
    return render(request, 'projects/single-project.html')